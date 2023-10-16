!pip install git+https://github.com/data-8/datascience.git

from datascience import *
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import pandas as pd

%matplotlib inline
import matplotlib.pyplot as plots
#plots.style.use('fivethirtyeight')
#plots.rcParams["patch.force_edgecolor"] = True


politics_csv = "https://raw.githubusercontent.com/mallikareddy22/CSK_DataScience/main/CSK%202022%20DS%20Materials/politics_apr2020.csv"
politics = Table().read_table(politics_csv)
politics

politics_women = politics.where("male", are.equal_to(0))
politics_men = politics.where("male", are.equal_to(1))
num_politics_women = politics_women.num_rows
num_politics = politics.num_rows
percentage_women = num_politics_women/num_politics * 100
percentage_women
    
politics_mw = politics.group("male")
politics_mw

politics_women_type = politics_women.group("government")
politics_women_type

politics_women_type.barh("government", "count")

politics_men_type = politics_men.group("government")
politics_men_type

politics_men_type.barh("government", "count")

military_politics = politics.where("militarycareer", are.equal_to(1))
military_politics_men = politics.where("male", are.equal_to(1))
military_politics_men_num = military_politics_men.where("militarycareer", are.equal_to(1))
military_politics_women = politics.where("male", are.equal_to(0))
military_politics_women_num = military_politics_women.where("militarycareer", are.equal_to(1))

military_politics_women_num

military_politics_men_num