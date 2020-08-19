import cv2
import os
count = 0

class v2i:
    def __init__(self, vid_path: str, output_path: str, count: int = 0):
        self.vid_path = vid_path
        self.output_path = output_path
        self.count = count
        
    def run(self):
        # out_path=os.path.abspath(f'{self.output_path}/../my_real_measure_all')
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        vid_cap = cv2.VideoCapture(self.vid_path)
        success, image = vid_cap.read()
        # count = 0
        # out_path=os.path.abspath(f'{self.output_path}/../my_real_measure_all')
        while success:
            cv2.imwrite(f"{out_path}/frame%d.jpg" % self.count, image)  # save frame as JPEG file
            success, image = vid_cap.read()
            print(f'Read a new frame {self.count}: ', success)
            self.count += 1
        return self.count

if __name__ == "__main__":
    count = 0
    
    path='measure_20200424_161325'
    count = v2i.run(vid_path=f'/home/jitesh/3d/data/my_measure/{path}.mp4',
        output_path=f'/home/jitesh/3d/data/my_measure/{path}',
        count=count)
    path='measure_20200424_161434'
    count = v2i.run(vid_path=f'/home/jitesh/3d/data/my_measure/{path}.mp4',
        output_path=f'/home/jitesh/3d/data/my_measure/{path}',
        count=count)
    path='measure_20200424_161657'
    count = v2i.run(vid_path=f'/home/jitesh/3d/data/my_measure/{path}.mp4',
        output_path=f'/home/jitesh/3d/data/my_measure/{path}',
        count=count)
    path='measure_20200424_162930'
    count = v2i.run(vid_path=f'/home/jitesh/3d/data/my_measure/{path}.mp4',
        output_path=f'/home/jitesh/3d/data/my_measure/{path}',
        count=count)
    path='measure_20200424_163027'
    count = v2i.run(vid_path=f'/home/jitesh/3d/data/my_measure/{path}.mp4',
        output_path=f'/home/jitesh/3d/data/my_measure/{path}',
        count=count)
