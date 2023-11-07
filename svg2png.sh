if [ "$#" -ne 1 ]; then
    echo "Usage:                    "
    echo "       $0 <<FilenameStub>>"
    echo "where the file to be converted is <<FileNameStub>>.svg and the output is <<FileNameStub>>.png"
    exit
fi


rsvg-convert -h 1000 $1.svg > videos/$1.png
