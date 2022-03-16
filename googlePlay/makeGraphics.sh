#!/bin/bash

# =================================================
# Variables
# =================================================
silent=0
tmpFile=/tmp/$(basename $0)
srcDir=./src
dstDir=./img

# =================================================
# Functions
# =================================================
function help() {
  cat<<EOF
NAME
       `basename $0` - SUMMARY

SYNOPSIS
       `basename $0` [-s] [-h] [-i dir] [-o dir]

DESCRIPTION
       INFO

       -s
              Silent mode

       -h
              Show this help

       -i dir
              Folder where repos the images are get (def: $srcDir)

       -o dir
              Folder where repos the images are stored (def: $dstDir)
EOF
}

function trace() {
  [ $silent -eq 0 ] && echo $* >&2
}

# =================================================
# Arguments
# =================================================
while getopts "hsi:o:" opt
do
  case $opt in
    h)
      help
      exit 0
      ;;
    s) silent=1 ;;
    i) srcDir=$OPTARG ;;
    o) dstDir=$OPTARG ;;
    *)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done
shift $(( OPTIND - 1 ))

# --- Check Arguments
errors=""

#[[ -z "$dir" ]] && errors="${errors}A folder must be specified. "

if [[ ! -z "$errors" ]]
then
  trace $errors
  exit 1
fi

# =================================================
# main
# =================================================
rm ${tmpFile}* 2>/dev/null

# Images with 16:9 aspect
# Portrait:
# - w : 320px
# - h : 
w=320
h=$(echo "$w*16/9"|bc -l)
echo "w: $w, h: $h"

for file in $(ls -1 $srcDir)
do
  fileName=$(echo $file|cut -d '.' -f 1,1)
  fileExt=$(echo $file|cut -d '.' -f 2,2)
  srcFile=${srcDir}/${file}
  dstFile=${dstDir}/${fileName}.9x16.${fileExt}
  echo "Converting ${srcFile} -> ${dstFile}"
  convert ${srcFile} -resize ${w}x${h} -background white -gravity center -extent ${w}x${h} ${dstFile}
done


w=1024
h=500

for file in $(ls -1 $srcDir)
do
  fileName=$(echo $file|cut -d '.' -f 1,1)
  fileExt=$(echo $file|cut -d '.' -f 2,2)
  srcFile=${srcDir}/${file}
  dstFile=${dstDir}/${fileName}.FeatureGraphic.${fileExt}
  echo "Converting ${srcFile} -> ${dstFile}"
  convert ${srcFile} -resize ${w}x${h} -background white -gravity center -extent ${w}x${h} ${dstFile}
done



rm ${tmpFile}* 2>/dev/null

