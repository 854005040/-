import paddlehub as hub
import warnings
import cv2
warnings.filterwarnings("ignore", category=Warning) # 过滤报警信息

ocr = hub.Module(name="chinese_ocr_db_crnn_mobile", enable_mkldnn=True)
screen=cv2.imread('C:/Users/Admin/Desktop/PY_document/image/1.png')
print(screen)
imgs = [screen,]
print(imgs)
results = ocr.recognize_text(
                            images=imgs,         # 图片数据，ndarray.shape 为 [H, W, C]，BGR格式；
                            use_gpu=False,            # 是否使用 GPU；若使用GPU，请先设置CUDA_VISIBLE_DEVICES环境变量
                            output_dir='ocr_result',  # 图片的保存路径，默认设为 ocr_result；
                            visualization=True,       # 是否将识别结果保存为图片文件；
                            box_thresh=0.7,           # 检测文本框置信度的阈值；
                            text_thresh=0.7)



print(results)







