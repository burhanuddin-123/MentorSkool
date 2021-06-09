# from loader import loader # Module name loader will be imported from the package loader
# from loader.loader import Loader   # directly class will be imported

from loader.loader import Loader

l = Loader("C:/Users/Burhanuddin/Study/Slack/Software_Development/products.csv")
l.load("Github","Product")

