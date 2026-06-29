echo "本程序将在当前目录安装并配置USFM所需要的环境和工具"
echo "正在配置python虚拟环境，将在系统中安装uv包管理器"

read -p "输入继续(Y/n):" data
if [[ $data == "n" || $data == "N" ]]; then
    echo "已取消安装"
    exit 0
fi

read -p "选择安装方式curl(输入c)或者wget(输入w):" data
if [[ $data == "c"]];
then
    curl -LsSf https://astral.sh/uv/install.sh | sh
else
    wget -qO- https://astral.sh/uv/install.sh | sh
fi

uv venv
source .venv/bin/activate
uv pip install json5

#echo "正在下载工具minecraft-nbt-editor"
#pip install click>=8.0.0 colorama>=0.4.4 rich>=12.0.0