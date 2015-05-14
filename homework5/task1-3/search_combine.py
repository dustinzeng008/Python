import searcher
import data_load
import indexer
import data_load

#data_load.get_traversal_data()
d = indexer.process_data("raw_data.pickle", "fortunes_shelve")
searcher.search("fortunes_shelve")

