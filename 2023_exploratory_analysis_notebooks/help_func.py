
import seaborn as sns

# sns.color_palette('colorblind')
# color blind seaborn palette, but want the two Rounce types w. similar color
pal_models = [(0.33725490196078434, 0.7058823529411765, 0.9137254901960784), # Rounce
               (0.8705882352941177, 0.5607843137254902, 0.0196078431372549), # Compagno
             (0.00784313725490196, 0.6196078431372549, 0.45098039215686275), # Zekollari
              (0.8, 0.47058823529411764, 0.7372549019607844), # OGGM_v16
              (0.984313725490196, 0.6862745098039216, 0.8941176470588236),  # OGGM-VAS
             (0.5803921568627451, 0.5803921568627451, 0.5803921568627451), # GLIMB
             (0.8352941176470589, 0.3686274509803922, 0.0), # 'Kraaijenbrink'
              (0.9254901960784314, 0.8823529411764706, 0.2), # JAMES
              sns.color_palette('dark')[5], # CISM2
             sns.color_palette('dark')[6],   # this is for the OGGM_v153 (which will be removed again anyways)
            (0.00392156862745098, 0.45098039215686275, 0.6980392156862745), #Huss
             ]
pal_models = sns.color_palette(pal_models)
model_order = ['Rounce', 'Compagno', 'Zekollari',
               'OGGM_v16', 'OGGM-VAS','GLIMB', 'Kraaijenbrink', 'James', 'CISM2','OGGM_v153', 'Huss']
model_order_anonymous = {'Rounce': 'model 1', 'Compagno': 'model 2',  'Zekollari' : 'model 3' , 
                         'OGGM_v16': 'model 4', 'OGGM-VAS': 'model 5', 'GLIMB': 'model 6', 'Kraaijenbrink': 'model 7', 
                        'James': 'model 8', 'CISM2': 'model 9', 'OGGM_v153': 'model 10', 'Huss': 'model 11'}





d_reg_num_name = {}
d_reg_num_name['01'] = 'Alaska'
d_reg_num_name['02'] = 'Western Canada & USA'
d_reg_num_name['03'] = 'Arctic Canada North'
d_reg_num_name['04'] = 'Arctic Canada South'
d_reg_num_name['05'] = 'Greenland'
d_reg_num_name['06'] = 'Iceland'
d_reg_num_name['07'] = 'Svalbard and Jan Mayen'
d_reg_num_name['08'] = 'Scandinavia'
d_reg_num_name['09'] = 'Russian Arctic'
d_reg_num_name['10'] = 'North Asia'
d_reg_num_name['11'] = 'Central Europe'
d_reg_num_name['12'] = 'Caucasus and Middle East'
d_reg_num_name['13'] = 'Central Asia'
d_reg_num_name['14'] = 'South Asia West'
d_reg_num_name['15'] = 'South Asia East'
d_reg_num_name['16'] = 'Low Latitudes'
d_reg_num_name['17'] = 'Southern Andes'
d_reg_num_name['18'] = 'New Zealand'
d_reg_num_name['19'] = 'Antarctic and Subantarctic'

d_reg_num_name_sh = {}
d_reg_num_name_sh['01'] = 'Alaska'
d_reg_num_name_sh['02'] = 'Western Canada\n& USA'
d_reg_num_name_sh['03'] = 'Arctic Canada North'
d_reg_num_name_sh['04'] = 'Arctic Canada South'
d_reg_num_name_sh['05'] = 'Greenland'
d_reg_num_name_sh['06'] = 'Iceland'
d_reg_num_name_sh['07'] = 'Svalbard and\nJan Mayen'
d_reg_num_name_sh['08'] = 'Scandinavia'
d_reg_num_name_sh['09'] = 'Russian Arctic'
d_reg_num_name_sh['10'] = 'North Asia'
d_reg_num_name_sh['11'] = 'Central Europe'
d_reg_num_name_sh['12'] = 'Caucasus and\nMiddle East'
d_reg_num_name_sh['13'] = 'Central Asia'
d_reg_num_name_sh['14'] = 'South Asia West'
d_reg_num_name_sh['15'] = 'South Asia East'
d_reg_num_name_sh['16'] = 'Low Latitudes'
d_reg_num_name_sh['17'] = 'Southern Andes'
d_reg_num_name_sh['18'] = 'New Zealand'
d_reg_num_name_sh['19'] = 'Antarctic and\nSubantarctic'