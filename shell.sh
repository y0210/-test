#!/bin/bash
echo "猜猜我最喜欢的歌手"
read test
case $test in
"周杰伦")
echo "他唱的太快了"
;;
"邓紫棋")
echo "高音小天后，原来你也喜欢"
;;
" 曾沛慈")
echo "四月分南京有他的演唱会要一起看吗"
;;
*)
echo "你根本并不知道我喜欢谁"
;;
esac

