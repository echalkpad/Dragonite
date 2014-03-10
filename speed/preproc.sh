#!/bin/bash
base=$1
for folder in `ls $base`
do
    img_folder=$base/$folder/pictures
    out_folder=$base/$folder/img
    mkdir $out_folder

    echo "Folder $img_folder"
    for f in `ls $img_folder`
    do
       img=$img_folder/$f 
       out_img=$out_folder/$f
       echo "Converting... $img -> $out_img"
       convert $img -resize 640x480 $out_img
    done
done
