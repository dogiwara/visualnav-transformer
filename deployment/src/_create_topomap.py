#!/usr/bin/env python3

import argparse
import os
from utils import msg_to_pil
import time

# ROS
import rospy
import rosbag

def remove_files_in_dir(dir_path: str):
    for f in os.listdir(dir_path):
        file_path = os.path.join(dir_path, f)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print("Failed to delete %s. Reason: %s" % (file_path, e))



def main(args: argparse.Namespace):
    topomap_name_dir = os.path.join(args.output_dir)
    if not os.path.isdir(topomap_name_dir):
        os.makedirs(topomap_name_dir)
    else:
        print(f"{topomap_name_dir} already exists. Removing previous images...")
        remove_files_in_dir(topomap_name_dir)

    bagfile = rosbag.Bag(args.bagfile_path)

    assert args.dt > 0, "dt must be positive"

    bag_to_image(bagfile, args.image_topic_name, topomap_name_dir, args.dt)


def bag_to_image(bag, image_topic, output_dir, dt):
    prev_time = 0
    img_idx = 0
    for topic, msg, time in bag.read_messages(topics=image_topic):
        if img_idx == 0 or (time - prev_time).to_sec() > dt:
            save_path = os.path.join(output_dir, f"{img_idx}.png")
            save_img = msg_to_pil(msg)
            save_img.save(save_path)
            img_idx += 1
            prev_time = time

    print(f"Saved {img_idx+1} images to {output_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=f"Code to generate topomaps from the image topic"
    )
    parser.add_argument(
        "--bagfile-path",
        "-b",
        type=str,
        help="path to bagfile",
    )
    parser.add_argument(
        "--output-dir",
        "-d",
        default="topomap",
        type=str,
        help="path to topological map images in ../topomaps/images directory (default: topomap)",
    )
    parser.add_argument(
        "--image-topic-name",
        "-i",
        default="camera/image_raw",
        type=str,
        help="image topic name (default: camera/image_raw)",
    )
    parser.add_argument(
        "--dt",
        "-t",
        default=3.,
        type=float,
        help=f"time between images sampled from the image topic (default: 3.0)",
    )
    args = parser.parse_args()

    main(args)
