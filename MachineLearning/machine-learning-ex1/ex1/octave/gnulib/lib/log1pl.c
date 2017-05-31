/* Natural logarithm of 1 plus argument.
   Copyright (C) 2011-2016 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

#include <config.h>

/* Specification.  */
#include <math.h>

#if HAVE_SAME_LONG_DOUBLE_AS_DOUBLE

long double
log1pl (long double x)
{
  return log1p (x);
}

#else

long double
log1pl (long double x)
{
  if (isnanl (x))
    return x;

  if (x <= -1.0L)
    {
      if (x == -1.0L)
        /* Return -Infinity.  */
        return - HUGE_VALL;
      else
        {
          /* Return NaN.  */
#if defined _MSC_VER || (defined __sgi && !defined __GNUC__)
          static long double zero;
          return zero / zero;
#else
          return 0.0L / 0.0L;
#endif
        }
    }

  if (x < -0.5L || x > 1.0L)
    return logl (1.0L + x);
  /* Here -0.5 <= x <= 1.0.  */

  if (x == 0.0L)
    /* Return a zero with the same sign as x.  */
    return x;

  /* Decompose x into
       1 + x = (1 + m/256) * (1 + y)
     where
       m is an integer, -128 <= m <= 256,
       y is a number, |y| <= 1/256.
     y is computed as
       y = (256 * x - m) / (256 + m).
     Then
       log(1+x) = log(m/256) + log(1+y)
     The first summand is a table lookup.
     The second summand is computed
       - either through the power series
           log(1+y) = y
                      - 1/2 * y^2
                      + 1/3 * y^3
                      - 1/4 * y^4
                      + 1/5 * y^5
                      - 1/6 * y^6
                      + 1/7 * y^7
                      - 1/8 * y^8
                      + 1/9 * y^9
                      - 1/10 * y^10
                      + 1/11 * y^11
                      - 1/12 * y^12
                      + 1/13 * y^13
                      - 1/14 * y^14
                      + 1/15 * y^15
                      - ...
       - or as log(1+y) = log((1+z)/(1-z)) = 2 * atanh(z)
         where z = y/(2+y)
         and atanh(z) is computed through its power series:
           atanh(z) = z
                      + 1/3 * z^3
                      + 1/5 * z^5
                      + 1/7 * z^7
                      + 1/9 * z^9
                      + 1/11 * z^11
                      + 1/13 * z^13
                      + 1/15 * z^15
                      + ...
         Since |z| <= 1/511 < 0.002, the relative contribution of the z^15
         term is < 1/15*0.002^14 < 2^-120 <= 2^-LDBL_MANT_DIG, therefore we
         can truncate the series after the z^13 term.  */

  {
    long double m = roundl (x * 256.0L);
    long double y = ((x * 256.0L) - m) / (m + 256.0L);
    long double z = y / (2.0L + y);

/* Coefficients of the power series for atanh(z).  */
#define ATANH_COEFF_1  1.0L
#define ATANH_COEFF_3  0.333333333333333333333333333333333333334L
#define ATANH_COEFF_5  0.2L
#define ATANH_COEFF_7  0.142857142857142857142857142857142857143L
#define ATANH_COEFF_9  0.1111111111111111111111111111111111111113L
#define ATANH_COEFF_11 0.090909090909090909090909090909090909091L
#define ATANH_COEFF_13 0.076923076923076923076923076923076923077L
#define ATANH_COEFF_15 0.066666666666666666666666666666666666667L

    long double z2 = z * z;
    long double atanh_z =
      ((((((ATANH_COEFF_13
            * z2 + ATANH_COEFF_11)
           * z2 + ATANH_COEFF_9)
          * z2 + ATANH_COEFF_7)
         * z2 + ATANH_COEFF_5)
        * z2 + ATANH_COEFF_3)
       * z2 + ATANH_COEFF_1)
      * z;

    /* logl_table[i] = log((i + 128) / 256).
       Computed in GNU clisp through
         (setf (long-float-digits) 128)
         (setq a 0L0)
         (setf (long-float-digits) 256)
         (dotimes (i 385)
           (format t "        ~D,~%"
                   (float (log (* (/ (+ i 128) 256) 1L0)) a)))  */
    static const long double logl_table[385] =
      {
        -0.693147180559945309417232121458176568075L,
        -0.6853650401178903604697692213970398044L,
        -0.677642994023980055266378075415729732197L,
        -0.669980121278410931188432960495886651496L,
        -0.662375521893191621046203913861404403985L,
        -0.65482831625780871022347679633437927773L,
        -0.647337644528651106250552853843513225963L,
        -0.639902666041133026551361927671647791137L,
        -0.632522558743510466836625989417756304788L,
        -0.625196518651437560022666843685547154042L,
        -0.617923759322357783718626781474514153438L,
        -0.61070351134887071814907205278986876216L,
        -0.60353502187025817679728065207969203929L,
        -0.59641755410139419712166106497071313106L,
        -0.58935038687830174459117031769420187977L,
        -0.582332814219655195222425952134964639978L,
        -0.575364144903561854878438011987654863008L,
        -0.568443702058988073553825606077313299585L,
        -0.561570822771226036828515992768693405624L,
        -0.554744857700826173731906247856527380683L,
        -0.547965170715447412135297057717612244552L,
        -0.541231138534103334345428696561292056747L,
        -0.534542150383306725323860946832334992828L,
        -0.527897607664638146541620672180936254347L,
        -0.52129692363328608707713317540302930314L,
        -0.514739523087127012297831879947234599722L,
        -0.50822484206593331675332852879892694707L,
        -0.50175232756031585480793331389686769463L,
        -0.495321437230025429054660050261215099L,
        -0.488931639131254417913411735261937295862L,
        -0.482582411452595671747679308725825054355L,
        -0.476273242259330949798142595713829069596L,
        -0.470003629245735553650937031148342064701L,
        -0.463773079495099479425751396412036696525L,
        -0.457581109247178400339643902517133157939L,
        -0.451427243672800141272924605544662667972L,
        -0.445311016655364052636629355711651820077L,
        -0.43923197057898186527990882355156990061L,
        -0.4331896561230192424451526269158655235L,
        -0.427183632062807368078106194920633178807L,
        -0.421213465076303550585562626925177406092L,
        -0.415278729556489003230882088534775334993L,
        -0.409379007429300711070330899107921801414L,
        -0.403513887976902632538339065932507598071L,
        -0.397682967666109433030550215403212372894L,
        -0.391885849981783528404356583224421075418L,
        -0.386122145265033447342107580922798666387L,
        -0.380391470556048421030985561769857535915L,
        -0.374693449441410693606984907867576972481L,
        -0.369027711905733333326561361023189215893L,
        -0.363393894187477327602809309537386757124L,
        -0.357791638638807479160052541644010369001L,
        -0.352220593589352099112142921677820359633L,
        -0.346680413213736728498769933032403617363L,
        -0.341170757402767124761784665198737642087L,
        -0.33569129163814153519122263131727209364L,
        -0.330241686870576856279407775480686721935L,
        -0.324821619401237656369001967407777741178L,
        -0.31943077076636122859621528874235306143L,
        -0.314068827624975851026378775827156709194L,
        -0.308735481649613269682442058976885699557L,
        -0.303430429419920096046768517454655701024L,
        -0.298153372319076331310838085093194799765L,
        -0.292904016432932602487907019463045397996L,
        -0.287682072451780927439219005993827431504L,
        -0.282487255574676923482925918282353780414L,
        -0.277319285416234343803903228503274262719L,
        -0.272177885915815673288364959951380595626L,
        -0.267062785249045246292687241862699949179L,
        -0.261973715741573968558059642502581569596L,
        -0.256910413785027239068190798397055267412L,
        -0.251872619755070079927735679796875342712L,
        -0.2468600779315257978846419408385075613265L,
        -0.24187253642048672427253973837916408939L,
        -0.2369097470783577150364265832942468196375L,
        -0.2319714654377751430492321958603212094726L,
        -0.2270574506353460848586128739534071682175L,
        -0.222167465341154296870334265401817316702L,
        -0.2173012756899813951520225351537951559L,
        -0.212458651214193401740613666010165016867L,
        -0.2076393647782445016154410442673876674964L,
        -0.202843192514751471266885961812429707545L,
        -0.1980699137620937948192675366153429027185L,
        -0.193319311003495979595900706211132426563L,
        -0.188591169807550022358923589720001638093L,
        -0.183885278770137362613157202229852743197L,
        -0.179201429457710992616226033183958974965L,
        -0.174539416351899677264255125093377869519L,
        -0.169899036795397472900424896523305726435L,
        -0.165280090939102924303339903679875604517L,
        -0.160682381690473465543308397998034325468L,
        -0.156105714663061654850502877304344269052L,
        -0.1515498981272009378406898175577424691056L,
        -0.1470147429618096590348349122269674042104L,
        -0.142500062607283030157283942253263107981L,
        -0.1380056730194437167017517619422725179055L,
        -0.1335313926245226231463436209313499745895L,
        -0.129077042275142343345847831367985856258L,
        -0.124642445207276597338493356591214304499L,
        -0.1202274269981598003244753948319154994493L,
        -0.115831815525121705099120059938680166568L,
        -0.1114554409253228268966213677328042273655L,
        -0.1070981355563671005131126851708522185606L,
        -0.1027597339577689347753154133345778104976L,
        -0.098440072813252519902888574928971234883L,
        -0.094138990913861910035632096996525066015L,
        -0.0898563291218610470766469347968659624282L,
        -0.0855919303354035139161469686670511961825L,
        -0.0813456394539524058873423550293617843895L,
        -0.077117303344431289769666193261475917783L,
        -0.072906770808087780565737488890929711303L,
        -0.0687138925480518083746933774035034481663L,
        -0.064538521137571171672923915683992928129L,
        -0.0603805109889074798714456529545968095868L,
        -0.0562397183228760777967376942769773768851L,
        -0.0521160011390140183616307870527840213665L,
        -0.0480092191863606077520036253234446621373L,
        -0.0439192339348354905263921515528654458042L,
        -0.0398459085471996706586162402473026835046L,
        -0.0357891078515852792753420982122404025613L,
        -0.0317486983145803011569962827485256299276L,
        -0.0277245480148548604671395114515163869272L,
        -0.0237165266173160421183468505286730579517L,
        -0.0197245053477785891192717326571593033246L,
        -0.015748356968139168607549511460828269521L,
        -0.0117879557520422404691605618900871263399L,
        -0.0078431774610258928731840424909435816546L,
        -0.00391389932113632909231778364357266484272L,
        0.0L,
        0.00389864041565732301393734309584290701073L,
        0.00778214044205494894746290006113676367813L,
        0.01165061721997527413559144280921434893315L,
        0.0155041865359652541508540460424468358779L,
        0.01934296284313093463590553454155047018545L,
        0.0231670592815343782287991609622899165794L,
        0.0269765876982020757480692925396595457815L,
        0.0307716586667536883710282075967721640917L,
        0.0345523815066597334073715005898328652816L,
        0.038318864302136599193755325123797290346L,
        0.042071213920687054375203805926962379448L,
        0.045809536031294203166679267614663342114L,
        0.049533935122276630882096208829824573267L,
        0.0532445145188122828658701937865287769396L,
        0.0569413764001384247590131015404494943015L,
        0.0606246218164348425806061320404202632862L,
        0.0642943507053972572162284502656114944857L,
        0.0679506619085077493945652777726294140346L,
        0.071593653187008817925605272752092034269L,
        0.075223421237587525698605339983662414637L,
        0.078840061707776024531540577859198294559L,
        0.082443669211074591268160068668307805914L,
        0.086034337341803153381797826721996075141L,
        0.0896121586896871326199514693784845287854L,
        0.093177224854183289768781353027759396216L,
        0.096729626458551112295571056487463437015L,
        0.1002694531636751493081301751297276601964L,
        0.1037967936816435648260618037639746883066L,
        0.1073117357890880506671750303711543368066L,
        0.1108143663402901141948061693232119280986L,
        0.1143047712800586336342591448151747734094L,
        0.1177830356563834545387941094705217050686L,
        0.1212492436328696851612122640808405265723L,
        0.1247034785009572358634065153808632684918L,
        0.128145822691930038174109886961074873852L,
        0.1315763577887192725887161286894831624516L,
        0.134995164537504830601983291147085645626L,
        0.138402322859119135685325873601649187393L,
        0.1417979118602573498789527352804727189846L,
        0.1451820098444978972819350637405643235226L,
        0.1485546943231371429098223170672938691604L,
        0.151916042025841975071803424896884511328L,
        0.1552661289111239515223833017101021786436L,
        0.1586050301766385840933711746258415752456L,
        0.161932820269313253240338285123614220592L,
        0.165249572895307162875611449277240313729L,
        0.1685553610298066669415865321701023169345L,
        0.171850256926659222340098946055147264935L,
        0.1751343321278491480142914649863898412374L,
        0.1784076574728182971194002415109419683545L,
        0.181670303107634678260605595617079739242L,
        0.184922338494011992663903592659249621006L,
        0.1881638324181829868259905803105539806714L,
        0.191394852999629454609298807561308873447L,
        0.194615467699671658858138593767269731516L,
        0.1978257433299198803625720711969614690756L,
        0.201025746060590741340908337591797808969L,
        0.204215541428690891503820386196239272214L,
        0.2073951943460705871587455788490062338536L,
        0.210564769107349637669552812732351513721L,
        0.2137243293977181388619051976331987647734L,
        0.216873938300614359619089525744347498479L,
        0.220013658305282095907358638661628360712L,
        0.2231435513142097557662950903098345033745L,
        0.226263678650453389361787082280390161607L,
        0.229374101064845829991480725046139871551L,
        0.232474878743094064920705078095567528222L,
        0.235566071312766909077588218941043410137L,
        0.2386477378501750099171491363522813392526L,
        0.241719936887145168144307515913513900104L,
        0.244782726417690916434704717466314811104L,
        0.247836163904581256780602765746524747999L,
        0.25088030628580941658844644154994089393L,
        0.253915209980963444137323297906606667466L,
        0.256940930897500425446759867911224262093L,
        0.259957524436926066972079494542311044577L,
        0.26296504550088135182072917321108602859L,
        0.265963548497137941339125926537543389269L,
        0.268953087345503958932974357924497845489L,
        0.271933715483641758831669494532999161983L,
        0.274905485872799249167009582983018668293L,
        0.277868451003456306186350032923401233082L,
        0.280822662900887784639519758873134832073L,
        0.28376817313064459834690122235025476666L,
        0.286705032803954314653250930842073965668L,
        0.289633292583042676878893055525668970004L,
        0.292553002686377439978201258664126644308L,
        0.295464212893835876386681906054964195182L,
        0.298366972551797281464900430293496918012L,
        0.301261330578161781012875538233755492657L,
        0.304147335467296717015819874720446989991L,
        0.30702503529491186207512454053537790169L,
        0.309894477722864687861624550833227164546L,
        0.31275571000389688838624655968831903216L,
        0.315608778986303334901366180667483174144L,
        0.318453731118534615810247213590599595595L,
        0.321290612453734292057863145522557457887L,
        0.324119468654211976090670760434987352183L,
        0.326940344995853320592356894073809191681L,
        0.329753286372467981814422811920789810952L,
        0.332558337300076601412275626573419425269L,
        0.335355541921137830257179579814166199074L,
        0.338144944008716397710235913939267433111L,
        0.340926586970593210305089199780356208443L,
        0.34370051385331844468019789211029452987L,
        0.346466767346208580918462188425772950712L,
        0.349225389785288304181275421187371759687L,
        0.35197642315717818465544745625943892599L,
        0.354719909102929028355011218999317665826L,
        0.357455888921803774226009490140904474434L,
        0.360184403575007796281574967493016620926L,
        0.362905493689368453137824345977489846141L,
        0.365619199560964711319396875217046453067L,
        0.368325561158707653048230154050398826898L,
        0.371024618127872663911964910806824955394L,
        0.373716409793584080821016832715823506644L,
        0.376400975164253065997877633436251593315L,
        0.379078352934969458390853345631019858882L,
        0.38174858149084833985966626493567607862L,
        0.384411698910332039734790062481290868519L,
        0.387067742968448287898902502261817665695L,
        0.38971675114002521337046360400352086705L,
        0.392358760602863872479379611988215363485L,
        0.39499380824086897810639403636498176831L,
        0.397621930647138489104829072973405554918L,
        0.40024316412701270692932510199513117008L,
        0.402857544701083514655197565487057707577L,
        0.405465108108164381978013115464349136572L,
        0.408065889808221748430198682969084124381L,
        0.410659924985268385934306203175822787661L,
        0.41324724855021933092547601552548590025L,
        0.415827895143710965613328892954902305356L,
        0.418401899138883817510763261966760106515L,
        0.42096929464412963612886716150679597245L,
        0.423530115505803295718430478017910109426L,
        0.426084395310900063124544879595476618897L,
        0.428632167389698760206812276426639053152L,
        0.43117346481837134085917247895559499848L,
        0.433708320421559393435847903042186017095L,
        0.436236766774918070349041323061121300663L,
        0.438758836207627937745575058511446738878L,
        0.441274560804875229489496441661301225362L,
        0.443783972410300981171768440588146426918L,
        0.446287102628419511532590180619669006749L,
        0.448783982827006710512822115683937186274L,
        0.451274644139458585144692383079012478686L,
        0.453759117467120506644794794442263270651L,
        0.456237433481587594380805538163929748437L,
        0.458709622626976664843883309250877913511L,
        0.461175715122170166367999925597855358603L,
        0.463635740963032513092182277331163919118L,
        0.466089729924599224558619247504769399859L,
        0.468537711563239270375665237462973542708L,
        0.470979715218791012546897856056359251373L,
        0.473415770016672131372578393236978550606L,
        0.475845904869963914265209586304381412175L,
        0.478270148481470280383546145497464809096L,
        0.480688529345751907676618455448011551209L,
        0.48310107575113582273837458485214554795L,
        0.485507815781700807801791077190788900579L,
        0.487908777319238973246173184132656942487L,
        0.490303988045193838150346159645746860531L,
        0.492693475442575255695076950020077845328L,
        0.495077266797851514597964584842833665358L,
        0.497455389202818942250859256731684928918L,
        0.499827869556449329821331415247044141512L,
        0.502194734566715494273584171951812573586L,
        0.504556010752395287058308531738174929982L,
        0.506911724444854354113196312660089270034L,
        0.509261901789807946804074919228323824878L,
        0.51160656874906207851888487520338193135L,
        0.51394575110223431680100608827421759311L,
        0.51627947444845449617281928478756106467L,
        0.518607764208045632152976996364798698556L,
        0.520930645624185312409809834659637709188L,
        0.52324814376454783651680722493487084164L,
        0.525560283522927371382427602307131424923L,
        0.527867089620842385113892217778300963557L,
        0.530168586609121617841419630845212405063L,
        0.532464798869471843873923723460142242606L,
        0.534755750616027675477923292032637111077L,
        0.537041465896883654566729244153832299024L,
        0.539321968595608874655355158077341155752L,
        0.54159728243274437157654230390043409897L,
        0.543867430967283517663338989065998323965L,
        0.546132437598135650382397209231209163864L,
        0.548392325565573162748150286179863158565L,
        0.550647117952662279259948179204913460093L,
        0.552896837686677737580717902230624314327L,
        0.55514150754050159271548035951590405017L,
        0.557381150134006357049816540361233647898L,
        0.559615787935422686270888500526826593487L,
        0.561845443262691817915664819160697456814L,
        0.564070138284802966071384290090190711817L,
        0.566289895023115872590849979337124343595L,
        0.568504735352668712078738764866962263577L,
        0.5707146810034715448536245647415894503L,
        0.572919753561785509092756726626261068625L,
        0.575119974471387940421742546569273429365L,
        0.577315365034823604318112061519496401506L,
        0.579505946414642223855274409488070989814L,
        0.58169173963462248252061075372537234071L,
        0.583872765580982679097413356975291104927L,
        0.586049045003578208904119436287324349516L,
        0.588220598517086043034868221609113995052L,
        0.590387446602176374641916708123598757576L,
        0.59254960960667159874199020959329739696L,
        0.594707107746692789514343546529205333192L,
        0.59685996110779383658731192302565801002L,
        0.59900818964608339938160002446165150206L,
        0.601151813189334836191674317068856441547L,
        0.603290851438084262340585186661310605647L,
        0.6054253239667168894375677681414899356L,
        0.607555250224541795501085152791125371894L,
        0.609680649536855273481833501660588408785L,
        0.611801541105992903529889766428814783686L,
        0.613917944012370492196929119645563790777L,
        0.616029877215514019647565928196700650293L,
        0.618137359555078733872689126674816271683L,
        0.620240409751857528851494632567246856773L,
        0.62233904640877874159710264120869663505L,
        0.62443328801189350104253874405467311991L,
        0.626523152931352759778820859734204069282L,
        0.628608659422374137744308205774183639946L,
        0.6306898256261987050837261409313532241L,
        0.63276666957103782954578646850357975849L,
        0.634839209173010211969493840510489008123L,
        0.63690746223706923162049442718119919119L,
        0.63897144645792072137962398326473680873L,
        0.64103117942093129105560133440539254671L,
        0.643086678603027315392053859585132960477L,
        0.645137961373584701665228496134731905937L,
        0.647185044995309550122320631377863036675L,
        0.64922794662510981889083996990531112227L,
        0.651266683314958103396333353349672108398L,
        0.653301272012745638758615881210873884572L,
        0.65533172956312763209494967856962559648L,
        0.657358072708360030141890023245936165513L,
        0.659380318089127826115336413370955804038L,
        0.661398482245365008260235838709650938148L,
        0.66341258161706625109695030429080128179L,
        0.665422632545090448950092610006660181147L,
        0.667428651271956189947234166318980478403L,
        0.669430653942629267298885270929503510123L,
        0.67142865660530232331713904200189252584L,
        0.67342267521216672029796038880101726475L,
        0.67541272562017673108090414397019748722L,
        0.677398823591806140809682609997348298556L,
        0.67938098479579735014710062847376425181L,
        0.681359224807903068948071559568089441735L,
        0.683333559111620688164363148387750369654L,
        0.68530400309891941654404807896723298642L,
        0.687270572070960267497006884394346103924L,
        0.689233281238808980324914337814603903233L,
        0.691192145724141958859604629216309755938L,
        0.693147180559945309417232121458176568075L
      };
    return logl_table[128 + (int)m] + 2.0L * atanh_z;
  }
}

#endif
