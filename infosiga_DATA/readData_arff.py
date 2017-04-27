import weka.core.converters as converters
import weka.core.jvm as jvm

jvm.start()
data = converters.load_any_file("fullData.arff")
data.class_is_last()

print(data)
