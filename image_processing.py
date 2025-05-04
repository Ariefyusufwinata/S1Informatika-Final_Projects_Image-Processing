import cv2
import os
from tqdm import tqdm

video_files = [
    "gA_1_s1_2019-03-08T09;31;15+01;00_rgb_face.mp4",
    "gA_1_s2_2019-03-08T09;21;03+01;00_rgb_face.mp4",
    "gA_1_s3_2019-03-14T14;31;08+01;00_rgb_face.mp4",
    "gA_1_s5_2019-03-14T14;26;17+01;00_rgb_face.mp4",
    "gA_1_s6_2019-03-08T09;15;15+01;00_rgb_face.mp4",
    "gA_2_s1_2019-03-08T10;01;44+01;00_rgb_face.mp4",
    "gA_2_s2_2019-03-08T09;50;49+01;00_rgb_face.mp4",
    "gA_2_s3_2019-03-13T09;23;42+01;00_rgb_face.mp4",
    "gA_2_s5_2019-03-13T09;19;23+01;00_rgb_face.mp4",
    "gA_2_s6_2019-03-08T09;44;39+01;00_rgb_face.mp4",
    "gA_3_s1_2019-03-08T10;27;38+01;00_rgb_face.mp4",
    "gA_3_s2_2019-03-08T10;16;48+01;00_rgb_face.mp4",
    "gA_3_s3_2019-03-13T09;41;01+01;00_rgb_face.mp4",
    "gA_3_s5_2019-03-13T09;36;25+01;00_rgb_face.mp4",
    "gA_3_s6_2019-03-08T10;12;10+01;00_rgb_face.mp4",
    "gA_4_s1_2019-03-13T10;36;15+01;00_rgb_face.mp4",
    "gA_4_s2_2019-03-13T10;43;06+01;00_rgb_face.mp4",
    "gA_4_s3_2019-03-13T11;00;49+01;00_rgb_face.mp4",
    "gA_4_s5_2019-03-13T10;56;52+01;00_rgb_face.mp4",
    "gA_4_s6_2019-03-13T10;51;44+01;00_rgb_face.mp4",
    "gA_5_s1_2019-03-08T10;57;00+01;00_rgb_face.mp4",
    "gA_5_s2_2019-03-08T10;46;46+01;00_rgb_face.mp4",
    "gA_5_s3_2019-03-13T09;10;35+01;00_rgb_face.mp4",
    "gA_5_s5_2019-03-13T09;06;49+01;00_rgb_face.mp4",
    "gA_5_s6_2019-03-08T10;40;35+01;00_rgb_face.mp4",
    "gB_6_s1_2019-03-11T13;55;14+01;00_rgb_face.mp4",
    "gB_6_s2_2019-03-11T13;46;14+01;00_rgb_face.mp4",
    "gB_6_s3_2019-03-13T13;41;02+01;00_rgb_face.mp4",
    "gB_6_s5_2019-03-13T13;37;11+01;00_rgb_face.mp4",
    "gB_6_s6_2019-03-11T13;41;36+01;00_rgb_face.mp4",
    "gB_7_s1_2019-03-11T14;22;01+01;00_rgb_face.mp4",
    "gB_7_s2_2019-03-11T14;12;25+01;00_rgb_face.mp4",
    "gB_7_s3_2019-03-13T13;59;54+01;00_rgb_face.mp4",
    "gB_7_s5_2019-03-13T13;55;52+01;00_rgb_face.mp4",
    "gB_7_s6_2019-03-11T14;08;04+01;00_rgb_face.mp4",
    "gB_8_s1_2019-03-11T15;01;33+01;00_rgb_face.mp4",
    "gB_8_s2_2019-03-11T14;38;44+01;00_rgb_face.mp4",
    "gB_8_s3_2019-03-13T14;13;40+01;00_rgb_face.mp4",
    "gB_8_s5_2019-03-13T14;10;09+01;00_rgb_face.mp4",
    "gB_9_s1_2019-03-07T16;36;24+01;00_rgb_face.mp4",
    "gB_9_s2_2019-03-07T16;21;20+01;00_rgb_face.mp4",
    "gB_9_s3_2019-03-07T16;29;41+01;00_rgb_face.mp4",
    "gB_9_s5_2019-03-07T16;31;48+01;00_rgb_face.mp4",
    "gB_9_s6_2019-03-07T16;16;22+01;00_rgb_face.mp4",
    "gB_10_s1_2019-03-11T15;24;54+01;00_rgb_face.mp4",
    "gB_10_s3_2019-03-12T10;40;46+01;00_rgb_face.mp4",
    "gB_10_s5_2019-03-12T10;35;20+01;00_rgb_face.mp4",
    "gC_11_s1_2019-03-04T09;33;18+01;00_rgb_face.mp4",
    "gC_11_s2_2019-03-04T09;25;33+01;00_rgb_face.mp4",
    "gC_11_s3_2019-03-12T10;15;32+01;00_rgb_face.mp4",
    "gC_11_s5_2019-03-12T09;08;15+01;00_rgb_face.mp4",
    "gC_11_s6_2019-03-04T09;20;21+01;00_rgb_face.mp4",
    "gC_12_s1_2019-03-13T10;23;45+01;00_rgb_face.mp4",
    "gC_12_s2_2019-03-13T10;14;41+01;00_rgb_face.mp4",
    "gC_12_s3_2019-03-14T10;00;44+01;00_rgb_face.mp4",
    "gC_12_s5_2019-03-14T09;56;52+01;00_rgb_face.mp4",
    "gC_12_s6_2019-03-13T10;09;40+01;00_rgb_face.mp4",
    "gC_13_s1_2019-03-04T10;26;12+01;00_rgb_face.mp4",
    "gC_13_s2_2019-03-04T10;11;37+01;00_rgb_face.mp4",
    "gC_13_s3_2019-03-12T10;06;34+01;00_rgb_face.mp4",
    "gC_13_s5_2019-03-12T10;03;00+01;00_rgb_face.mp4",
    "gC_13_s6_2019-03-04T10;06;53+01;00_rgb_face.mp4",
    "gE_28_s1_2019-03-15T10;23;30+01;00_rgb_face.mp4",
    "gE_28_s2_2019-03-15T10;12;30+01;00_rgb_face.mp4",
    "gF_23_s1_2019-03-04T16;21;10+01;00_rgb_face.mp4",
    "gF_23_s2_2019-03-04T16;09;26+01;00_rgb_face.mp4",
    "gF_23_s3_2019-03-11T09;31;59+01;00_rgb_face.mp4",
    "gF_23_s3_2019-03-14T13;54;34+01;00_rgb_face.mp4",
    "gZ_32_s1_2019-04-08T12;01;26+02;00_rgb_face.mp4",
    "gZ_32_s1_2019-04-08T16;35;53+02;00_rgb_face.mp4",
    "gZ_32_s2_2019-04-08T11;53;07+02;00_rgb_face.mp4",
    "gZ_32_s2_2019-04-08T16;28;10+02;00_rgb_face.mp4",
    "gZ_32_s3_2019-04-04T09;52;12+02;00_rgb_face.mp4"
]

input_base_path = "input"
output_base_path = "output"
target_fps = 29

for filename in video_files:
    parts = filename.split("_")
    group = parts[0]     # e.g., 'gA', 'gB'
    number = parts[1]    # e.g., '1', '2'
    session = parts[2]   # e.g., 's1', 's2'

    input_folder = os.path.join(input_base_path, group, number)
    video_path = os.path.join(input_folder, filename)

    output_folder = os.path.join(output_base_path, group, number, session)
    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Failed to open video: {video_path}")
        continue

    original_fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_interval = max(1, round(original_fps / target_fps))

    frame_number = 0
    saved_frame_number = 0

    print(f"\nProcessing: {filename}")
    with tqdm(total=total_frames, desc=f"{group}_{number}_{session}", unit="frame") as pbar:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            if frame_number % frame_interval == 0:
                prefix = f"{group}_{number}_{session}"
                frame_filename = os.path.join(output_folder, f"{prefix}_frame_{saved_frame_number}.jpg")

                cv2.imwrite(frame_filename, frame)
                saved_frame_number += 1

            pbar.update(1)
            frame_number += 1

    cap.release()

cv2.destroyAllWindows()