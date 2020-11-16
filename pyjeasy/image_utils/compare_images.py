import os
import sys as x
import cv2
import printj
import numpy as np
from tqdm import tqdm
from pyjeasy.file_utils import get_all_filepaths_of_extension, make_dir_if_not_exists
from pyjeasy.image_utils import show_image

def write_text(img, text, position=(10,500), color=(255, 255, 255)):
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = position
    fontScale              = .9
    fontColor              = color
    lineType               = 2

    cv2.putText(img,text, 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        lineType)

    return img

def compare_images_4dir(
    path1: str, path2: str, path3: str, path4: str, 
    compare_path: str, 
    show_preview: bool=False, 
    create_images: bool=False, 
    create_video: bool=False,
    n: str=None, 
    t1: str=None, 
    t2: str=None, 
    t3: str=None, 
    t4: str=None, 
    iterations: int=None,
    bbox_thresh: float=None,
    concate_type: str="hh"):
    # file_list1_compare = [file for file in os.listdir(path1) if ".jpg" in file.lower()]
    # file_list2_compare = [file for file in os.listdir(path2) if ".jpg" in file.lower()]
    # file_list3_compare = [file for file in os.listdir(path3) if ".jpg" in file.lower()]
    # file_list4_compare = [file for file in os.listdir(path4) if ".jpg" in file.lower()]
    file_list_compare_list = [None]
    for path in [path1, path2, path3, path4]:
        file_list_compare_list.append(get_all_filepaths_of_extension(
            dirpath=path, extension=[".jpg", ".jpeg", ".png"]))
        
    images = []
    # f1_path = []
    # f2_path = []
    # f3_path = []
    # f4_path = []
    # file_list2_edited = file_list_compare_list[1].copy()
    # # Edit path 2
    # for i, file1 in enumerate(file_list_compare_list[1]):
    #     if file1 in file_list_compare_list[2]:
    #         file_path = os.path.abspath(f'{path2}/{file1}') 
    #     else:
    #         file_path = os.path.abspath(f'{path2}/../bad/{file1}')
    #     f2_path.append(file_path)   
    
    # for i, file2 in enumerate(file_list_compare_list[2]):
    #     if not file2 in file_list2_edited:
    #         file_list2_edited.append(file2)
    #         file_path = os.path.abspath(f'{path2}/{file2}') 
    #         f2_path.append(file_path) 
    # # Edit path 1
    # for i, file2 in enumerate(file_list2_edited):
    #     if file2 in file_list_compare_list[1]:
    #         file_path = os.path.abspath(f'{path1}/{file2}') 
    #         printj.red(i)
    #     else:
    #         file_path = os.path.abspath(f'{path1}/../bad/{file2}')
    #         printj.green(i)
    #     f1_path.append(file_path)   
    
    # for i, file3 in enumerate(file_list_compare_list[3]):
    #     file_path = os.path.abspath(f'{path3}/{file3}')
    #     f3_path.append(file_path)
    # for i, file4 in enumerate(file_list_compare_list[4]): 
    #     file_path = os.path.abspath(f'{path4}/{file4}')
    #     f4_path.append(file_path)
        
           
    # for i, (file1_path, file2_path, file3_path, file4_path) in tqdm(enumerate(zip(f1_path, f2_path, f3_path, f4_path)), desc=f'Loading imageset {n}'):
    for i, (file1_path, file2_path, file3_path, file4_path) in tqdm(enumerate(
        zip(file_list_compare_list[1], file_list_compare_list[2], file_list_compare_list[3], file_list_compare_list[4])), 
                                                                    desc=f'Comparing images', total=len(file_list_compare_list[1])
                                                                    ,colour= '#66cc66',):
        filename1 = file1_path.split('/')[-1]
        filename2 = file2_path.split('/')[-1]
        filename3 = file3_path.split('/')[-1]
        filename4 = file4_path.split('/')[-1]
        assert filename1 == filename2
        assert filename3 == filename2
        assert filename3 == filename4
        images1 = cv2.imread(file1_path)
        images2 = cv2.imread(file2_path)
        images3 = cv2.imread(file3_path)
        images4 = cv2.imread(file4_path)
        compare_images1 = cv2.hconcat([images1, images2])
        compare_images2 = cv2.hconcat([images3, images4])
        if concate_type =="hh":
            compare_images = cv2.hconcat([compare_images1, compare_images2])
            compare_images = cv2.resize(compare_images, (1920, 840)) 
            compare_images = cv2.copyMakeBorder( compare_images, top=50, bottom=100, left=0, right=0, borderType=0)
            compare_images = write_text(compare_images, f'{filename1}', (10, 950))  #, (100, 250, 250))
            if t1:
                compare_images = write_text(compare_images, t1, (10, 40), (50, 102, 250))
            if t2:
                compare_images = write_text(compare_images, t2, (500, 40), (155, 250, 155))
            if t3:
                compare_images = write_text(compare_images, t3, (980, 40), (100, 250, 250))
            if t4:
                compare_images = write_text(compare_images, t4, (1460, 40), (250, 202, 102))
            if bbox_thresh:
                compare_images = write_text(compare_images, f'bbox_thresh = {bbox_thresh}', (1600, 980))
            if iterations:
                compare_images = write_text(compare_images, f' {iterations}k iterations ', (1600, 950))
            
            compare_images = cv2.line(compare_images, (480, 0), (480, 890), (255, 222, 110), thickness=1)
            compare_images = cv2.line(compare_images, (960, 0), (960, 890), (255, 222, 110), thickness=1)
            compare_images = cv2.line(compare_images, (1440, 0), (1440, 890), (255, 222, 110), thickness=1)
            

        elif concate_type =="hv":
            compare_images = cv2.vconcat([compare_images1, compare_images2])
            compare_images = cv2.resize(compare_images, (1920, 840)) 
            compare_images = cv2.copyMakeBorder( compare_images, top=50, bottom=100, left=0, right=0, borderType=0)
            compare_images = write_text(compare_images, f'{filename1}', (10, 950))  #, (100, 250, 250))
            if t1:
                compare_images = write_text(compare_images, t1, (10, 40), (50, 102, 250))
            if t2:
                compare_images = write_text(compare_images, t2, (990, 40), (155, 250, 155))
            if t3:
                compare_images = write_text(compare_images, t3, (10, 920), (100, 250, 250))
            if t4:
                compare_images = write_text(compare_images, t4, (990, 920), (250, 102, 50))
            if bbox_thresh:
                compare_images = write_text(compare_images, f'bbox_thresh = {bbox_thresh}', (1600, 980))
            if iterations:
                compare_images = write_text(compare_images, f' {iterations}k iterations ', (1600, 950))
        else:
            printj.red(f'concate_type = {concate_type} is not implemented yet.\n Valid options for concate_type are: "hh" and "hv"')
            raise NotImplementedError
            
        images.append(compare_images)
        #Show image
        if show_preview==True:
            quit_flag = show_image(compare_images, window_name='compare images')
            if quit_flag:
                cv2.destroyAllWindows()
                break
        if create_images==True:
            make_dir_if_not_exists(compare_path)
            cv2.imwrite(f"{compare_path}/{filename1}", compare_images)
            
def compare_images_2dir(
    path1: str, path2: str, 
    # path3: str, path4: str, 
    compare_path: str, 
    show_preview: bool=False, 
    create_images: bool=False, 
    create_video: bool=False,
    n: str=None, 
    t1: str=None, 
    t2: str=None, 
    # t3: str=None, 
    # t4: str=None, 
    iterations: int=None,
    bbox_thresh: float=None,
    concate_type: str="h"):
    file_list_compare_list = [None]
    for path in [path1, path2]:
        file_list_compare_list.append(get_all_filepaths_of_extension(
            dirpath=path, extension=[".jpg", ".jpeg", ".png"]))
        
    images = []
           
    for i, (file1_path, file2_path) in tqdm(enumerate(
        zip(file_list_compare_list[1], file_list_compare_list[2])), 
        desc=f'Comparing images', total=len(file_list_compare_list[1]),
        colour= '#66cc66'):
        filename1 = file1_path.split('/')[-1]
        filename2 = file2_path.split('/')[-1]
        assert filename1 == filename2
        images1 = cv2.imread(file1_path)
        images2 = cv2.imread(file2_path)
        # compare_images1 = cv2.hconcat([images1, images2])
        # compare_images2 = cv2.hconcat([images3, images4])
        if concate_type =="h":
            compare_images = cv2.hconcat([images1, images2])
            compare_images = cv2.resize(compare_images, (1920, 840)) 
            compare_images = cv2.copyMakeBorder( compare_images, top=50, bottom=100, left=0, right=0, borderType=0)
            compare_images = write_text(compare_images, f'{filename1}', (10, 950))  #, (100, 250, 250))
            if t1:
                compare_images = write_text(compare_images, t1, (10, 40), (50, 102, 250))
            if t2:
                compare_images = write_text(compare_images, t2, (980, 40), (155, 250, 155))
            if bbox_thresh:
                compare_images = write_text(compare_images, f'bbox_thresh = {bbox_thresh}', (1600, 980))
            if iterations:
                compare_images = write_text(compare_images, f' {iterations}k iterations ', (1600, 950))
            
            compare_images = cv2.line(compare_images, (960, 0), (960, 890), (255, 222, 110), thickness=1)
            

        elif concate_type =="v":
            compare_images = cv2.vconcat([compare_images1, compare_images2])
            compare_images = cv2.resize(compare_images, (1920, 840)) 
            compare_images = cv2.copyMakeBorder( compare_images, top=50, bottom=100, left=0, right=0, borderType=0)
            compare_images = write_text(compare_images, f'{filename1}', (10, 950))  #, (100, 250, 250))
            if t1:
                compare_images = write_text(compare_images, t1, (10, 40), (50, 102, 250))
            if t2:
                compare_images = write_text(compare_images, t2, (990, 40), (155, 250, 155))
            if bbox_thresh:
                compare_images = write_text(compare_images, f'bbox_thresh = {bbox_thresh}', (1600, 980))
            if iterations:
                compare_images = write_text(compare_images, f' {iterations}k iterations ', (1600, 950))
        else:
            printj.red(f'concate_type = {concate_type} is not implemented yet.\n Valid options for concate_type are: "hh" and "hv"')
            raise NotImplementedError
            
        images.append(compare_images)
        #Show image
        if show_preview==True:
            quit_flag = show_image(compare_images, window_name='compare images')
            if quit_flag:
                cv2.destroyAllWindows()
                break
        if create_images==True:
            make_dir_if_not_exists(compare_path)
            cv2.imwrite(f"{compare_path}/{filename1}", compare_images)
            
            
    
def compare_images_2dir0(path1, path2, compare_path, show_preview=False, create_images=False, create_video=False, n=None):
    file_list1_compare = os.listdir(path1)
    file_list2_compare = os.listdir(path2)
    images = []
    f1_path = []
    f2_path = []
    file_list2_edited = file_list1_compare.copy()
    # Edit path 2
    for i, file1 in enumerate(file_list1_compare):
        if file1 in file_list2_compare:
            file_path = os.path.abspath(f'{path2}/{file1}') 
        else:
            file_path = os.path.abspath(f'{path2}/../bad/{file1}')
        f2_path.append(file_path)   
    
    for i, file2 in enumerate(file_list2_compare):
        if not file2 in file_list2_edited:
            file_list2_edited.append(file2)
            file_path = os.path.abspath(f'{path2}/{file2}') 
            f2_path.append(file_path) 
    # Edit path 1
    for i, file2 in enumerate(file_list2_edited):
        if file2 in file_list1_compare:
            file_path = os.path.abspath(f'{path1}/{file2}') 
            printj.red(i)
        else:
            file_path = os.path.abspath(f'{path1}/../bad/{file2}')
            printj.green(i)
        f1_path.append(file_path)   
        
    for i, (file1_path, file2_path) in tqdm(enumerate(zip(f1_path, f2_path)), desc=f'Loading imageset {n}'):
        filename1 = file1_path.split('/')[-1]
        filename2 = file2_path.split('/')[-1]
        assert filename1 == filename2
        images1 = cv2.imread(file1_path)
        images2 = cv2.imread(file2_path)
        # assert images1.shape == images2.shape
        # if images1.shape[0]
        # dataname1 = file1_path.split('/')[-3].split('_')[6] +'_'+ file1_path.split('/')[-3].split('_')[7]
        # dataname2 = file2_path.split('/')[-3].split('_')[6] +'_'+ file2_path.split('/')[-3].split('_')[7]
        iterations = 20
        # iterations = round(int(file2_path.split('/')[-3].split('_')[8])/1000)
        # bbox_thresh = file2_path.split('/')[-3].split('_')[9]
        bbox_thresh = 0.2
        # printj.red(file1_path)
        # printj.yellow(file2_path)
        # sys.exit()
        # if filename1!= '209001_102_PC040686.JPG':
        #     continue
        ############################
        # printj.yellow(filename1)
        compare_images = cv2.hconcat([images1, images2])
        # compare_images = cv2.resize(compare_images, (960, 540)) 
        compare_images = cv2.resize(compare_images, (1920, 840)) 
        compare_images = cv2.copyMakeBorder( compare_images, top=50, bottom=100, left=0, right=0, borderType=0)
        # compare_images = write_text(compare_images, f'hook_sim_{dataname1}', (10, 40), (50, 102, 250))
        # compare_images = write_text(compare_images, f'hook_sim_{dataname2}', (990, 40), (155, 250, 155))
        # compare_images = write_text(compare_images, f'seg+key: hookpole model', (10, 40), (50, 102, 250))
        # compare_images = write_text(compare_images, f'seg+key: hook model', (990, 40), (155, 250, 155))
        compare_images = write_text(compare_images, f'bolt_3-4 Aug1', (10, 40), (50, 102, 250))
        compare_images = write_text(compare_images, f'bolt_3-4 Aug2', (990, 40), (155, 250, 155))
        # compare_images = write_text(compare_images, f'Img_{i}', (10, 920), (100, 250, 250))
        compare_images = write_text(compare_images, f'{filename1}', (10, 920), (100, 250, 250))
        compare_images = write_text(compare_images, f'bbox_thresh = {bbox_thresh}', (1600, 920))
        compare_images = write_text(compare_images, f' {iterations}k iterations ', (1600, 950))
        images.append(compare_images)
        #Show image
        if show_preview==True:
            cv2.imshow('compare images', compare_images)
            # cv2.waitKey(10000)
            key = cv2.waitKey(0) & 0xFF
            # printj.blue(key)
            if key == ord('q'):
                quit_flag = True
                cv2.destroyAllWindows()
                break
            # cv2.destroyAllWindows()
        if create_images==True:
            if not os.path.exists(compare_path):
                os.makedirs(compare_path)
            cv2.imwrite(f"{compare_path}/{filename1}", compare_images)
            cv2.waitKey(0)
            
            
if __name__ == "__main__":
    path1 = '/home/jitesh/3d/data/test_data/hexagon_bolts/img_ram-bolt_0_1x_final.pth_thres0.2_10_27_16_test'
    path2 = '/home/jitesh/3d/data/test_data/hexagon_bolts/img_bolt_1_1x_0019999.pth_thres0.2_10_27_16_test'
    path3 = '/home/jitesh/3d/data/test_data/hexagon_bolts/img_bolt_0_1x_0019999.pth_thres0.2_10_27_16_test'
    path4 = '/home/jitesh/3d/data/test_data/hexagon_bolts/img_b4_5_1x_0019999.pth_thres0.2_10_27_16_test'
    compare_path = '/home/jitesh/3d/data/test_data/hexagon_bolts/compare_b_ri_ja2_v2'
    compare_images_4dir(
        path1=path1, 
        path2=path2, 
        path3=path3, 
        path4=path4, 
        compare_path=compare_path, 
        show_preview=True, 
        # create_images=True, 
        # create_video=True,
        )
    # x()
    # compare_2good_images(
    #     path1=path1, 
    #     path2=path2, 
    #     compare_path=compare_path, 
    #     # show_preview=True, 
    #     create_images=True, 
    #     # create_video=True,
    #     )