import qrcode
img = qrcode.make('https://www.youtube.com/watch?v=rbGRguSUTP0&list=RDGMEMCMFH2exzjBeE_zAHHJOdxgVMrbGRguSUTP0&start_radio=1')
type(img)
img.save("some_file.png")