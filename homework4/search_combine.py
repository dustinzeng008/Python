import searcher
import data_load
import indexer

d=indexer.process_data("raw_data.pickle","fortunes_shelve")
searcher.search("fortunes_shelve")
