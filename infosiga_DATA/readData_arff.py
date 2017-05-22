import weka.core.converters as converters
import weka.clusterers as cluterer
import weka.core.jvm as jvm

jvm.start()
data = converters.load_any_file("INFOMAPA_AGOSTO_2016_csv.csv")
data.class_is_last()


print(data)
