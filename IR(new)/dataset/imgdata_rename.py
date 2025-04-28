import os
import re
def rename_img():    
    data_dir="/dataset"
    cur_dir=os.getcwd()+data_dir
    dataset_type=os.listdir(cur_dir)
    print(dataset_type)
    for dir1 in dataset_type:
        path1=cur_dir+"/"+dir1
        lis1=os.listdir(path1)
        for dir2 in lis1:
            path2=path1+"/"+dir2
            lis2=os.listdir(path2)
            print("Renaming Images in "+dir2)
            for i in range(len(lis2)):
                img_path=path2+"/"+lis2[i]
                img_prefix=dir2[(dir2.rindex("___")+3):].replace(" ","_")
                new_img_path=path2+"/"+ img_prefix +"_"+str(i)+".jpeg"

                os.rename(img_path,new_img_path)
                print(lis2[i],"   -------->    ",img_prefix +"_"+str(i)+".jpeg")
        
    print("Script Execution Completed")
if __name__=='__main__':
    rename_img()
