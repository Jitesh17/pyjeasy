import cv2
import os
count = 0

class v2i:
    def run(vid_path, img_path, count: int = 0):
        out_path=os.path.abspath(f'{img_path}/../my_real_measure_all')
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        vid_cap = cv2.VideoCapture(vid_path)
        success, image = vid_cap.read()
        # count = 0
        out_path=os.path.abspath(f'{img_path}/../my_real_measure_all')
        while success:
            cv2.imwrite(f"{out_path}/frame%d.jpg" % count, image)  # save frame as JPEG file
            success, image = vid_cap.read()
            print(f'Read a new frame {count}: ', success)
            count += 1
        return count

if __name__ == "__main__":
    count = 0
    
    path='measure_20200424_161325'
    count = v2i.run(vid_path=f'/home/jitesh/3d/data/my_measure/{path}.mp4',
        img_path=f'/home/jitesh/3d/data/my_measure/{path}',
        count=count)
    path='measure_20200424_161434'
    count = v2i.run(vid_path=f'/home/jitesh/3d/data/my_measure/{path}.mp4',
        img_path=f'/home/jitesh/3d/data/my_measure/{path}',
        count=count)
    path='measure_20200424_161657'
    count = v2i.run(vid_path=f'/home/jitesh/3d/data/my_measure/{path}.mp4',
        img_path=f'/home/jitesh/3d/data/my_measure/{path}',
        count=count)
    path='measure_20200424_162930'
    count = v2i.run(vid_path=f'/home/jitesh/3d/data/my_measure/{path}.mp4',
        img_path=f'/home/jitesh/3d/data/my_measure/{path}',
        count=count)
    path='measure_20200424_163027'
    count = v2i.run(vid_path=f'/home/jitesh/3d/data/my_measure/{path}.mp4',
        img_path=f'/home/jitesh/3d/data/my_measure/{path}',
        count=count)
