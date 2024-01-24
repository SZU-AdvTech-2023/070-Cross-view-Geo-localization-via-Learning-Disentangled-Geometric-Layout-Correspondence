### 项目结构

---|utils.py

---|train.py

---|test.py

---|interface.py

---|GeoDTR.py

---|data_preparation.py

---|check_cvusa_duplicate.py

---|datasets

​	---|layoutsim.py

​	---|cvusa.py

​	---|cvact.py

​	---|_init_py

​	---|CVUSA

​		---|streetview   街景图象

​			---|panos

​				---|存放图像文件图像

​			---|annotations

​				---|存放图像文件图像

​		---|splits   就是存放数据索引的地方

​			---|val-19zl.csv

​			---|train-19zl.csv

​		---|polarmap  这就是航拍图bingmap文件夹极坐标变换后的文件

​			---|19

​				---|存放图像文件图像

​		---|bingmap

​			---|19

​				---|存放图像文件图像

​	---|CVACT

​		---|ACT_data.mat   不可缺少的配置文件哦

​		---|ANU_data_test

​			---|streetview_processed   streetview的及坐标变换图

​				---|存放图像文件图像

​			---|streetview

​				---|存放图像文件图像

​			---satview_polish

​				---|存放图像文件图像

​			---|ploarmap   satview_polish的极坐标变换图

​				---|存放图像文件图像

​		---|ANU_data_small

​			---|streetview_processed   streetview的及坐标变换图

​				---|存放图像文件图像

​			---|streetview

​				---|存放图像文件图像

​			---satview_polish

​				---|存放图像文件图像

​			---|ploarmap   satview_polish的极坐标变换图

​				---|存放图像文件图像

### 环境配置

numpy

Pytorch >= 1.11

torchvision >= 0.12

tqdm

scipy

PIL



### 数据处理

数据集使用CVUSA和CVACT。

1、生成极坐标变换图

使用SAFA论文对数据集的处理方法，在运行代码前，使用提供的 data_preparation.py 文件对数据集进行预处理。

2、 CVUSA数据集查重

用check_cvusa_duplicate.py文件删除其中的重复项，原理就是MD5码。



### 项目执行

训练

```bash
python train.py \
--dataset CVUSA \
--data_dir path-to-your-data/ \
--n_des 8 \
--TR_heads 4 \
--TR_layers 2 \
--layout_sim strong \
--sem_aug strong \
--pt \
--cf
```

验证

```bash
python test.py \
--dataset CVUSA \
--data_dir path-to-your-data/ \
--model_path path-to-your-pretrained-weight
```
