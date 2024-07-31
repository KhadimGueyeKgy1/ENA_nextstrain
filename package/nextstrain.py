import os 


class nextstrain :

    def precess(input_dir, virus_name):
        if virus_name =='monkeypox':
            os.system("cd package/monkeypox/data ; sed -i -e 's/XXXX/2017/g' metadata.tsv ") # year ref
            os.system("cd package/monkeypox/data ;  sed -i -e 's/XX/01/g' metadata.tsv ")
            os.system('nextstrain build --cpus 1 '+input_dir+' --configfile config/config_mpxv.yaml')
        else : 
            os.system ('nextstrain build --cpus 1 '+input_dir)
    

    def view():
        os.system('nextstrain view auspice_res')
        
