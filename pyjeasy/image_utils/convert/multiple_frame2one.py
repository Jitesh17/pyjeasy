# -*- coding: utf-8 -*-
"""
Author: Jitesh Gosar
"""
import glob
import numpy as np
import cv2


   
def compare_2good_images(path1, path2, compare_path, show_preview=False, create_images=False, create_video=False, n=''):
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
        assert images1.shape == images2.shape
        
        dataname1 = file1_path.split('/')[-3].split('_')[6] +'_'+ file1_path.split('/')[-3].split('_')[7]
        dataname2 = file2_path.split('/')[-3].split('_')[6] +'_'+ file2_path.split('/')[-3].split('_')[7]
        iterations = round(int(file2_path.split('/')[-3].split('_')[8])/1000)
        bbox_thresh = file2_path.split('/')[-3].split('_')[9]
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
        compare_images = write_text(compare_images, f'crop-2 model ', (10, 40), (50, 102, 250))
        compare_images = write_text(compare_images, f'seg+key-1 model', (990, 40), (155, 250, 155))
        # compare_images = write_text(compare_images, f'Img_{i}', (10, 920), (100, 250, 250))
        compare_images = write_text(compare_images, f'{filename1}', (10, 920), (100, 250, 250))
        # compare_images = write_text(compare_images, f'bbox_thresh = {bbox_thresh}', (1600, 920))
        # compare_images = write_text(compare_images, f' {iterations}k iterations ', (1600, 950))
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
    
    path1 = '/home/jitesh/3d/data/coco_data/hook_test/level_01_08_17_09_Keypoints_data7_0.1_0029999_0.5_s1024_vis_infer_output_50_1x/good'
    path2 = '/home/jitesh/3d/data/coco_data/hook_test/level_01_08_17_09_Keypoints_real_data8_0029999_0.5_s1024_vis_infer_output_50_1x/infer_key_seg'
    compare_path = '/home/jitesh/3d/data/coco_data/hook_test/compare_crop_vs_seg&key2'
    compare_2good_images(
        path1=path1, 
        path2=path2, 
        compare_path=compare_path, 
        # show_preview=True, 
        create_images=True, 
        # create_video=True,
        )