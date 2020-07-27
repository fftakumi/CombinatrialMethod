import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

from combinatorial import affine

magnification = 1
rotation = 0
dx = 0
dy = 0
horizontal_flip = 1
vertical_flip = 1
imageData1_opacity = 0.5
imageData2_max = 0
imageData2_min = 0
imageData1_max = 0
imageData1_min = 0
imageData2_opacity = 0.5
layout_image_step = 10
plot_sample_num = 1000


def imageData1MaxChanged(sb):
    global imageData1_max
    imageData1_max = sb.value()
    ii_image_data1.setImage(np.where(current_image_data1 <= imageData1_max, current_image_data1, 0))


def imageData2MaxChanged(sb):
    global imageData2_max
    imageData2_max = sb.value()
    ii_image_data2.setLevels([imageData2_max, imageData2_min])


def imageData1MinChanged(sb):
    global imageData1_min
    imageData1_min = sb.value()
    ii_image_data1.setImage(np.where(imageData1_min <= current_image_data1, current_image_data1, 0))


def imageData2MinChanged(sb):
    global imageData2_min
    imageData2_min = sb.value()
    ii_image_data2.setLevels([imageData2_max, imageData2_min])


def imageData1AlphaChanged(sb):
    global imageData1_opacity
    imageData1_opacity = sb.value()
    ii_image_data1.setOpts(opacity=imageData1_opacity)


def imageData2AlphaChanged(sb):
    global imageData2_opacity
    imageData2_opacity = sb.value()
    ii_image_data2.setOpts(opacity=imageData2_opacity)


def imageData1RotationChanged(sb):
    global current_image_data1, rotation, dx, dy
    rotation = sb.value()
    current_image_data1 = affine.affine(image_data1, magnification=magnification, rotation=np.deg2rad(rotation), tx=dx,
                                        ty=dy,
                                        hf=horizontal_flip, vf=vertical_flip)
    ii_image_data1.setImage(current_image_data1)
    imageData1_imageData2RandomPlot()
    imageData1MaxChanged(imageData1MaxSpinBox)
    imageData1MinChanged(imageData1MinSpinBox)
    imageData1AlphaChanged(imageData1AplhaSpinBox)
    imageData2AlphaChanged(imageData2AplhaSpinBox)


def imageData1dxChanged(sb):
    global current_image_data1, rotation, dx, dy
    dx = sb.value()
    current_image_data1 = affine.affine(image_data1, magnification=magnification, rotation=np.deg2rad(rotation), tx=dx,
                                        ty=dy,
                                        hf=horizontal_flip, vf=vertical_flip)
    ii_image_data1.setImage(current_image_data1)
    imageData1_imageData2RandomPlot()
    imageData1MaxChanged(imageData1MaxSpinBox)
    imageData1MinChanged(imageData1MinSpinBox)
    imageData1AlphaChanged(imageData1AplhaSpinBox)
    imageData2AlphaChanged(imageData2AplhaSpinBox)


def imageData1dyChanged(sb):
    global current_image_data1, rotation, dx, dy
    dy = sb.value()
    current_image_data1 = affine.affine(image_data1, magnification=magnification, rotation=np.deg2rad(rotation), tx=dx,
                                        ty=dy,
                                        hf=horizontal_flip, vf=vertical_flip)
    ii_image_data1.setImage(current_image_data1)
    imageData1_imageData2RandomPlot()
    imageData1MaxChanged(imageData1MaxSpinBox)
    imageData1MinChanged(imageData1MinSpinBox)
    imageData1AlphaChanged(imageData1AplhaSpinBox)
    imageData2AlphaChanged(imageData2AplhaSpinBox)


def imageData1RotationChanging(sb):
    global current_image_data1, rotation, dx, dy
    rotation = sb.value()
    current_image_data1 = affine.affine(image_data1, magnification=magnification, rotation=np.deg2rad(rotation), tx=dx,
                                        ty=dy,
                                        hf=horizontal_flip, vf=vertical_flip)
    ii_image_data1.setImage(current_image_data1)
    imageData1_imageData2RandomPlot()


def imageData1DXChanging(sb):
    global current_image_data1, rotation, dx, dy
    dx = sb.value()
    current_image_data1 = affine.affine(image_data1, magnification=magnification, rotation=np.deg2rad(rotation), tx=dx,
                                        ty=dy,
                                        hf=horizontal_flip, vf=vertical_flip)
    ii_image_data1.setImage(current_image_data1)
    imageData1_imageData2RandomPlot()


def imageData1DYChanging(sb):
    global current_image_data1, rotation, dx, dy
    dy = sb.value()
    current_image_data1 = affine.affine(image_data1, magnification=magnification, rotation=np.deg2rad(rotation), tx=dx,
                                        ty=dy,
                                        hf=horizontal_flip, vf=vertical_flip)
    ii_image_data1.setImage(current_image_data1)
    imageData1_imageData2RandomPlot()


def imageData1HorizontalFlip():
    global current_image_data1, horizontal_flip
    horizontal_flip *= -1
    current_image_data1 = affine.affine(image_data1, magnification=magnification, rotation=np.deg2rad(rotation), tx=dx,
                                        ty=dy,
                                        hf=horizontal_flip, vf=vertical_flip)
    ii_image_data1.setImage(current_image_data1)
    imageData1_imageData2RandomPlot()
    imageData1MaxChanged(imageData1MaxSpinBox)
    imageData1MinChanged(imageData1MinSpinBox)
    imageData1AlphaChanged(imageData1AplhaSpinBox)
    imageData2AlphaChanged(imageData2AplhaSpinBox)


def imageData1VerticalFlip():
    global current_image_data1, vertical_flip
    vertical_flip *= -1
    current_image_data1 = affine.affine(image_data1, magnification=magnification, rotation=np.deg2rad(rotation), tx=dx,
                                        ty=dy,
                                        hf=horizontal_flip, vf=vertical_flip)
    ii_image_data1.setImage(current_image_data1)
    imageData1_imageData2RandomPlot()
    imageData1MaxChanged(imageData1MaxSpinBox)
    imageData1MinChanged(imageData1MinSpinBox)
    imageData1AlphaChanged(imageData1AplhaSpinBox)
    imageData2AlphaChanged(imageData2AplhaSpinBox)


def getImagePlotData(imageData1, imageData2):
    data1 = imageData1
    data2 = imageData2
    data1_height, data1_width = data1.shape
    data2_height, data2_width = data2.shape
    read_height = min(data1_height, data2_height)
    read_width = min(data1_width, data2_width)
    read_x, read_y = np.mgrid[:read_height, :read_width]
    read_data1 = data1[read_x, read_y].reshape(-1, )
    read_data2 = data2[read_x, read_y].reshape(-1, )
    return read_data1, read_data2


def imageData1_imageData2RandomPlot():
    data1, data2 = getImagePlotData(current_image_data1, image_data2)
    random_index = np.random.choice(np.arange(data1.shape[0]), plot_sample_num, replace=False)
    imageData1_imageData2_spi.setData(x=data1[random_index], y=data2[random_index])


def imageData1_imageData2FullPlot():
    data1, data2 = getImagePlotData(current_image_data1, image_data2)
    imageData1_imageData2_spi.setData(x=data1, y=data2)


def imageData1_imageData2PlotYMaxChanged(sb):
    imageData1_imageData2_pw.setYRange(sb.value(), imageData1_imageData2PlotYMinSpinBox.value())


def imageData1_imageData2PlotYMinChanged(sb):
    imageData1_imageData2_pw.setYRange(imageData1_imageData2PlotYMaxSpinBox.value(), sb.value())


def imageData1_imageData2PlotXMaxChanged(sb):
    imageData1_imageData2_pw.setXRange(sb.value(), imageData1_imageData2PlotXMinSpinBox.value())


def imageData1_imageData2PlotXMinChanged(sb):
    imageData1_imageData2_pw.setXRange(imageData1_imageData2PlotXMaxSpinBox.value(), sb.value())


def sampleNumSpinBoxChanged(sb):
    global plot_sample_num
    plot_sample_num = sb.value()
    imageData1_imageData2RandomPlot()


# Interpret image data as row-major instead of col-major
pg.setConfigOptions(imageAxisOrder='row-major')

# メインウィンドウセット
app = QtGui.QApplication([])

win = QtGui.QMainWindow()
win.setWindowTitle('Combinatorial -image analysys')
cw = QtGui.QWidget()
layout = QtGui.QGridLayout()
cw.setLayout(layout)
win.setCentralWidget(cw)
win.show()
win.resize(1200, 700)

# データ読み込み、画像表示
vb = pg.ViewBox(invertY=True)
image_data1 = np.loadtxt('./data/bp.dat')
current_image_data1 = affine.affine(image_data1, magnification=magnification, rotation=rotation, tx=dx, ty=dx)

image_data2 = np.loadtxt('./data/theta.dat')
ii_image_data2 = pg.ImageItem(image_data2, opacity=0.5, levels=(-0.3, 0.3))
vb.addItem(ii_image_data2)
ii_image_data1 = pg.ImageItem(current_image_data1, opacity=0.5)
vb.addItem(ii_image_data1)

vb.autoRange()
vb.setAspectLocked(True)
imgpw = pg.PlotWidget()
imgpw.addItem(vb)
layout.addWidget(imgpw, 0, 0, layout_image_step, layout_image_step)

# スピンボックス追加
imageData1MaxLabel = QtGui.QLabel('Data1 Max')
layout.addWidget(imageData1MaxLabel, layout_image_step, 0, 1, 2)
imageData1MaxSpinBox = pg.SpinBox(value=np.floor(np.max(image_data1)))
imageData1MaxSpinBox.setOpts(compactHeight=False)
layout.addWidget(imageData1MaxSpinBox, layout_image_step, 2, 1, 3)
imageData1MaxSpinBox.sigValueChanged.connect(imageData1MaxChanged)

imageData2MaxLabel = QtGui.QLabel('Data2 Max')
layout.addWidget(imageData2MaxLabel, layout_image_step, 5, 1, 2)
imageData2MaxSpinBox = pg.SpinBox(value=imageData2_max)
imageData2MaxSpinBox.setOpts(compactHeight=False)
layout.addWidget(imageData2MaxSpinBox, layout_image_step, 7, 1, 3)
imageData2MaxSpinBox.sigValueChanged.connect(imageData2MaxChanged)

imageData1MinLabel = QtGui.QLabel('Data1 Min')
layout.addWidget(imageData1MinLabel, layout_image_step + 1, 0, 1, 2)
imageData1MinSpinBox = pg.SpinBox(value=np.ceil(np.min(image_data1)))
imageData1MinSpinBox.setOpts(compactHeight=False)
layout.addWidget(imageData1MinSpinBox, layout_image_step + 1, 2, 1, 3)
imageData1MinSpinBox.sigValueChanged.connect(imageData1MinChanged)

imageData2MinLabel = QtGui.QLabel('Data2 Min')
layout.addWidget(imageData2MinLabel, layout_image_step + 1, 5, 1, 2)
imageData2MinSpinBox = pg.SpinBox(value=imageData2_min)
imageData2MinSpinBox.setOpts(compactHeight=False)
layout.addWidget(imageData2MinSpinBox, layout_image_step + 1, 7, 1, 3)
imageData2MinSpinBox.sigValueChanged.connect(imageData2MinChanged)

imageData1AlphaLabel = QtGui.QLabel('Data1 Alpha')
layout.addWidget(imageData1AlphaLabel, layout_image_step + 2, 0, 1, 2)
imageData1AplhaSpinBox = pg.SpinBox(value=0.5)
imageData1AplhaSpinBox.setOpts(compactHeight=False)
layout.addWidget(imageData1AplhaSpinBox, layout_image_step + 2, 2, 1, 3)
imageData1AplhaSpinBox.sigValueChanged.connect(imageData1AlphaChanged)

imageData2AlphaLabel = QtGui.QLabel('Data2 Alpha')
layout.addWidget(imageData2AlphaLabel, layout_image_step + 2, 5, 1, 2)
imageData2AplhaSpinBox = pg.SpinBox(value=0.5)
imageData2AplhaSpinBox.setOpts(compactHeight=False)
layout.addWidget(imageData2AplhaSpinBox, layout_image_step + 2, 7, 1, 3)
imageData2AplhaSpinBox.sigValueChanged.connect(imageData2AlphaChanged)

imageData1RotationLabel = QtGui.QLabel('Data1 Rotation')
layout.addWidget(imageData1RotationLabel, layout_image_step + 3, 0, 1, 2)
imageData1RotationSpinBox = pg.SpinBox(value=0, step=1)
imageData1RotationSpinBox.setOpts(compactHeight=False)
layout.addWidget(imageData1RotationSpinBox, layout_image_step + 3, 2, 1, 3)
imageData1RotationSpinBox.sigValueChanged.connect(imageData1RotationChanged)
# bpRotationSpinBox.sigValueChanging.connect(bpRotationChanging)

imageData1dxLabel = QtGui.QLabel('Data1 Move x')
layout.addWidget(imageData1dxLabel, layout_image_step + 4, 0, 1, 2)
imageData1dxSpinBox = pg.SpinBox(value=0, step=1)
imageData1dxSpinBox.setOpts(compactHeight=False)
layout.addWidget(imageData1dxSpinBox, layout_image_step + 4, 2, 1, 3)
imageData1dxSpinBox.sigValueChanged.connect(imageData1dxChanged)
# bpDXSpinBox.sigValueChanging.connect(bpDXChanging)

imageData1dyLabel = QtGui.QLabel('Data1 Move y')
layout.addWidget(imageData1dyLabel, layout_image_step + 5, 0, 1, 2)
imageData1dySpinBox = pg.SpinBox(value=0, step=1)
imageData1dySpinBox.setOpts(compactHeight=False)
layout.addWidget(imageData1dySpinBox, layout_image_step + 5, 2, 1, 3)
imageData1dySpinBox.sigValueChanged.connect(imageData1dyChanged)
# bpDYSpinBox.sigValueChanging.connect(bpDYChanging)

imageData1HorizontalFlipBtn = QtGui.QPushButton('Data1 Hrizontal Flip')
layout.addWidget(imageData1HorizontalFlipBtn, layout_image_step + 6, 0, 1, 2)
imageData1HorizontalFlipBtn.clicked.connect(imageData1HorizontalFlip)

imageData1VerticalFlipBtn = QtGui.QPushButton('Data1 Vertical Plot')
layout.addWidget(imageData1VerticalFlipBtn, layout_image_step + 6, 3, 1, 2)
imageData1VerticalFlipBtn.clicked.connect(imageData1VerticalFlip)

# フルエンス-ファラデープロット
imageData1_imageData2_spi = pg.ScatterPlotItem()
imageData1_imageData2_pw = pg.PlotWidget()
imageData1_imageData2_pw.addItem(imageData1_imageData2_spi)
imageData1_imageData2_pw.setYRange(0.3, -0.3)
layout.addWidget(imageData1_imageData2_pw, 0, layout_image_step, layout_image_step, layout_image_step)

plotBtn = QtGui.QPushButton('Plot')
layout.addWidget(plotBtn, layout_image_step + 5, 5, 1, 2)
plotBtn.clicked.connect(imageData1_imageData2RandomPlot)

fullPlotBtn = QtGui.QPushButton('Full Plot')
layout.addWidget(fullPlotBtn, layout_image_step + 5, 8, 1, 2)
fullPlotBtn.clicked.connect(imageData1_imageData2FullPlot)

imageData1_imageData2PlotYMaxLabel = QtGui.QLabel('Data1-Data2 Plot YMax')
layout.addWidget(imageData1_imageData2PlotYMaxLabel, layout_image_step, layout_image_step, 1, 2)
imageData1_imageData2PlotYMaxSpinBox = pg.SpinBox(value=0.5)
imageData1_imageData2PlotYMaxSpinBox.setOpts(compactHeight=False)
layout.addWidget(imageData1_imageData2PlotYMaxSpinBox, layout_image_step, layout_image_step + 2, 1, 3)
imageData1_imageData2PlotYMaxSpinBox.sigValueChanged.connect(imageData1_imageData2PlotYMaxChanged)

imageData1_imageData2PlotYMinLabel = QtGui.QLabel('Data1-Data2 Plot YMin')
layout.addWidget(imageData1_imageData2PlotYMinLabel, layout_image_step, layout_image_step + 5, 1, 2)
imageData1_imageData2PlotYMinSpinBox = pg.SpinBox(value=-0.5)
imageData1_imageData2PlotYMinSpinBox.setOpts(compactHeight=False)
layout.addWidget(imageData1_imageData2PlotYMinSpinBox, layout_image_step, layout_image_step + 7, 1, 3)
imageData1_imageData2PlotYMinSpinBox.sigValueChanged.connect(imageData1_imageData2PlotYMinChanged)

imageData1_imageData2PlotXMaxLabel = QtGui.QLabel('Dara1-Data2 Plot XMax')
layout.addWidget(imageData1_imageData2PlotXMaxLabel, layout_image_step + 1, layout_image_step, 1, 2)
imageData1_imageData2PlotXMaxSpinBox = pg.SpinBox(value=50)
imageData1_imageData2PlotXMaxSpinBox.setOpts(compactHeight=False)
layout.addWidget(imageData1_imageData2PlotXMaxSpinBox, layout_image_step + 1, layout_image_step + 2, 1, 3)
imageData1_imageData2PlotXMaxSpinBox.sigValueChanged.connect(imageData1_imageData2PlotXMaxChanged)

imageData1_imageData2PlotXMinLabel = QtGui.QLabel('Data1-Data2 Plot XMinx')
layout.addWidget(imageData1_imageData2PlotXMinLabel, layout_image_step + 1, layout_image_step + 5, 1, 2)
imageData1_imageData2PlotXMinSpinBox = pg.SpinBox(value=0)
imageData1_imageData2PlotXMinSpinBox.setOpts(compactHeight=False)
layout.addWidget(imageData1_imageData2PlotXMinSpinBox, layout_image_step + 1, layout_image_step + 7, 1, 3)
imageData1_imageData2PlotXMinSpinBox.sigValueChanged.connect(imageData1_imageData2PlotXMinChanged)

sampleNumLabel = QtGui.QLabel('Random Sample Num')
layout.addWidget(sampleNumLabel, layout_image_step + 2, layout_image_step, 1, 2)
sampleNumSpinBox = pg.SpinBox(value=plot_sample_num)
sampleNumSpinBox.setOpts(compactHeight=False, int=True, step=50)
layout.addWidget(sampleNumSpinBox, layout_image_step + 2, layout_image_step + 7, 1, 3)
sampleNumSpinBox.sigValueChanged.connect(sampleNumSpinBoxChanged)

## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
