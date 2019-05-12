# -*- coding: utf-8 -*-
from doorclass import Door
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import *

class myyScene(QGraphicsView):

    def der(self, glass_colour, doorx, doory,
            doorx2, doory2, sidedoor,
            botfitx, botfit_colour, botfit_colour2,
            botfitx2, supportbfx, supportbfw, supportbfl,
            supportbf_colour,
            supportbfx2, supportbfw2, supportbfl2,
            supportbf_colour2,
            topfitx, topfit_colour,
            topfitx2, topfit_colour2,
            supporttfx, supporttfw, supporttfl, supporttf_colour,
            supporttfx2, supporttfw2, supporttfl2, supporttf_colour2,
            hinge_code, hinge_code2,
            hingex, hingex2, hingeq,
            doorhandle_code, doorhandlex, doorhandlex2,
            doorhandle_code2, doorhandlex_2, doorhandlex2_2,
            pushhandle_code, pushhandle_name,
            pushhandlex, pushhandlel, pushhandle_code2,
            pushhandle_name2, pushhandlex2, pushhandlel2,
            doorlock_code, doorlockx, doorlocky, doorlockw, doorlockl,
            doorlock_code2, doorlockx2, doorlocky2, doorlockw2,
            doorlockl2, knob_code, knob_code2, upx, upy, rightx, righty, leftx,
            lefty, lefProfL, RProfL, leftCapL, leftCapN, rightCapL, rightCapN,
            upProfN, upCapN, downProfN, downCapN):
        self.graphicsView = QGraphicsView(self)
        self.graphicsView.setGeometry(QRect(435, 10, 700, 550))
        self.graphicsView.setObjectName("graphicsView")
        self.scene = QGraphicsScene(self)
        self.graphicsView.scale(0.15, 0.15)
        self.graphicsView.setScene(self.scene)
        if upy == 0:
            zazor2 = 0
        else:
            zazor2 = 5
        if doorx2 == 0:
            zazorx = 0
        else:
            zazorx = 5

        if leftx != 0:
            left_glass = QGraphicsRectItem(0 - leftx - 5, 0 - upy - zazor2,
                                           leftx, lefty)
            left_glass.setPen(QPen(Qt.black,  5, Qt.SolidLine))
            grad_5 = QLinearGradient(0, 0, 1000, 10)
            if glass_colour == 'Матовое':
                grad_5.setColorAt(0.0, QtGui.QColor(240, 255, 255))
                grad_5.setColorAt(1.0, QtGui.QColor(220, 220, 220))
            else:
                grad_5.setColorAt(0.0, QtGui.QColor("darkCyan"))
                grad_5.setColorAt(1.0, QtGui.QColor("cyan"))
            left_glass.setBrush(QBrush(grad_5))
            self.scene.addItem(left_glass)

        if rightx != 0:
            if upy == 0:
                zazor = 0
            else:
                zazor = 5
            right_glass = QGraphicsRectItem(doorx + 5 + doorx2 + 5,
                                            0 - upy - zazor, rightx, righty)
            right_glass.setPen(QPen(Qt.black,  5, Qt.SolidLine))
            grad_4 = QLinearGradient(0, 0, 1000, 10)
            if glass_colour == 'Матовое':
                grad_4.setColorAt(0.0, QtGui.QColor(240, 255, 255))
                grad_4.setColorAt(1.0, QtGui.QColor(220, 220, 220))
            else:
                grad_4.setColorAt(0.0, QtGui.QColor("darkCyan"))
                grad_4.setColorAt(1.0, QtGui.QColor("cyan"))
            right_glass.setBrush(QBrush(grad_4))
            self.scene.addItem(right_glass)

        if upy != 0:
            up_glass = QGraphicsRectItem(0, 0 - upy - 5, upx, upy)
            up_glass.setPen(QPen(Qt.black,  5, Qt.SolidLine))
            grad_3 = QLinearGradient(0, 0, 1000, 10)
            if glass_colour == 'Матовое':
                grad_3.setColorAt(0.0, QtGui.QColor(240, 255, 255))
                grad_3.setColorAt(1.0, QtGui.QColor(220, 220, 220))
            else:
                grad_3.setColorAt(0.0, QtGui.QColor("darkCyan"))
                grad_3.setColorAt(1.0, QtGui.QColor("cyan"))
            up_glass.setBrush(QBrush(grad_3))
            self.scene.addItem(up_glass)

        door_glass = QGraphicsRectItem(0,0,doorx,doory)
        door_glass.setPen(QPen(Qt.black,  5, Qt.SolidLine))
        grad = QLinearGradient(0, 0, 1000, 10)
        if glass_colour == 'Матовое':
            grad.setColorAt(0.0, QtGui.QColor(240, 255, 255))
            grad.setColorAt(1.0, QtGui.QColor(220, 220, 220))
        else:
            grad.setColorAt(0.0, QtGui.QColor("darkCyan"))
            grad.setColorAt(1.0, QtGui.QColor("cyan"))
        door_glass.setBrush(QBrush(grad))
        self.scene.addItem(door_glass)


        #up_glass = QGraphicsRectItem(0,-350,1000,345)
        #up_glass.setBrush(QColor('yellow'))
        #self.scene.addItem(up_glass)

        if doorx2 != 0:
            door_glass2 = QGraphicsRectItem(doorx+5,0,doorx2,doory2)
            door_glass2.setPen(QPen(Qt.black,  5, Qt.SolidLine))
            grad_2 = QLinearGradient(0, 0, 2500, 10)
            if glass_colour == 'Матовое':
                grad_2.setColorAt(0.0, QtGui.QColor(220, 220, 220))
                grad_2.setColorAt(1.0, QtGui.QColor(240, 255, 255))
            else:
                grad_2.setColorAt(0.0, QtGui.QColor("darkCyan"))
                grad_2.setColorAt(1.0, QtGui.QColor("cyan"))
            door_glass2.setBrush(QBrush(grad_2))
            self.scene.addItem(door_glass2)

        if botfitx != 0:
            botFit = QGraphicsRectItem(botfitx,doory-51,161,51)
            if botfit_colour == 'ТР':
                botFit.setBrush(QColor('yellow'))
            else:
                botFit.setBrush(QColor('darkGray'))
            self.scene.addItem(botFit)

        if botfitx2 != 0:
            botFit2 = QGraphicsRectItem(botfitx2,doory-51,161,51)
            if botfit_colour2 == 'ТР':
                botFit2.setBrush(QColor('yellow'))
            else:
                botFit2.setBrush(QColor('darkGray'))
            self.scene.addItem(botFit2)

        if supportbfx != 0:
            supportbf = QGraphicsRectItem(supportbfx,doory+10,
                                        supportbfw,supportbfl)
            if supportbf_colour == 'TP':
                supportbf.setBrush(QColor('yellow'))
            else:
                supportbf.setBrush(QColor('grey'))
            self.scene.addItem(supportbf)

        if supportbfx2 != 0:
            supportbf2 = QGraphicsRectItem(supportbfx2,doory2+10,
                                           supportbfw2,supportbfl2)
            if supportbf_colour2 == 'TP':
                supportbf2.setBrush(QColor('yellow'))
            else:
                supportbf2.setBrush(QColor('grey'))
            self.scene.addItem(supportbf2)

        if topfitx != 0:
            top_fit = QGraphicsRectItem(topfitx,0,161,51)
            if topfit_colour == 'ТР':
                top_fit.setBrush(QColor('yellow'))
            else:
                top_fit.setBrush(QColor('grey'))
            self.scene.addItem(top_fit)

        if topfitx2 != 0:
            top_fit2 = QGraphicsRectItem(topfitx2,0,161,51)
            if topfit_colour2 == 'ТР':
                top_fit2.setBrush(QColor('yellow'))
            else:
                top_fit2.setBrush(QColor('grey'))
            self.scene.addItem(top_fit2)

        if supporttfx != 0:
            supporttf = QGraphicsRectItem(supporttfx,0-supporttfl-5,
                              supporttfw,supporttfl)
            if supporttf_colour == 'TP':
                supporttf.setBrush(QColor('yellow'))
            else:
                supporttf.setBrush(QColor('grey'))
            self.scene.addItem(supporttf)

        if supporttfx2 != 0:
            supporttf2 = QGraphicsRectItem(supporttfx2,
            0-supporttfl2-5,supporttfw2,supporttfl2)
            if supporttf_colour2 == 'TP':
                supporttf2.setBrush(QColor('yellow'))
            else:
                supporttf2.setBrush(QColor('grey'))
            self.scene.addItem(supporttf2)

        if hingex != 0:
            hinge1 = QGraphicsRectItem(hingex,250,62,89)
            hinge2 = QGraphicsRectItem(hingex,doory-312,62,89)
            if hinge_code[-2:] == 'TP':
                hinge1.setBrush(QColor('yellow'))
                hinge2.setBrush(QColor('yellow'))
            else:
                hinge1.setBrush(QColor('grey'))
                hinge2.setBrush(QColor('grey'))
            self.scene.addItem(hinge1)
            self.scene.addItem(hinge2)

        if hingex2 != 0:
            hinge1_2 = QGraphicsRectItem(hingex2,250,62,89)
            hinge2_2 = QGraphicsRectItem(hingex2,doory-312,62,89)
            if hinge_code2[-2:] == 'TP':
                hinge1_2.setBrush(QColor('yellow'))
                hinge2_2.setBrush(QColor('yellow'))
            else:
                hinge1_2.setBrush(QColor('grey'))
                hinge2_2.setBrush(QColor('grey'))
            self.scene.addItem(hinge1_2)
            self.scene.addItem(hinge2_2)

        if hingeq != 2:
            hinge3 = QGraphicsRectItem(hingex,doory/2-45,62,89)
            if hinge_code[-2:] == 'TP':
                hinge3.setBrush(QColor('yellow'))
            else:
                hinge3.setBrush(QColor('grey'))
            self.scene.addItem(hinge3)
            if doorx2 != 0:
                hinge3_2 = QGraphicsRectItem(hingex2,doory/2-45,62,89)
                if hinge_code2[-2:] == 'TP':
                    hinge3_2.setBrush(QColor('yellow'))
                else:
                    hinge3_2.setBrush(QColor('grey'))
                self.scene.addItem(hinge3_2)

        if doorhandlex != 0:
            doorhandle = QGraphicsRectItem(doorhandlex,doory/2-25,120,50)
            doorhandlearm = QGraphicsRectItem(doorhandlex2,doory/2-10,170,20)
            if doorhandle_code[-2:] == 'TP':
                doorhandle.setBrush(QColor('yellow'))
                doorhandlearm.setBrush(QColor('yellow'))
            else:
                doorhandle.setBrush(QColor('grey'))
                doorhandlearm.setBrush(QColor('grey'))
            self.scene.addItem(doorhandle)
            self.scene.addItem(doorhandlearm)

        if doorhandlex_2 != 0:
            doorhandle2 = QGraphicsRectItem(doorhandlex_2, doory/2-25,120,50)
            if doorhandle_code2[-2:] == 'TP':
                doorhandle2.setBrush(QColor('yellow'))
            else:
                doorhandle2.setBrush(QColor('grey'))
            self.scene.addItem(doorhandle2)
            doorhandlearm2 = QGraphicsRectItem(doorhandlex2_2,doory/2-10,170,20)
            if doorhandle_code2[-2:] == 'TP':
                doorhandlearm2.setBrush(QColor('yellow'))
            else:
                doorhandlearm2.setBrush(QColor('grey'))
            self.scene.addItem(doorhandlearm2)

        if pushhandlex != 0:
            if pushhandle_name[2:5] == '626':
                pushhandle = QGraphicsRectItem(pushhandlex, doory/2 - pushhandlel/2, 32, pushhandlel)
                if pushhandlex == 68:
                    pushhandle_horizontal = QGraphicsRectItem(pushhandlex, doory/2 + pushhandlel/2 - 32, 450, 32)
                else:
                    pushhandle_horizontal = QGraphicsRectItem(pushhandlex - 418, doory/2 + pushhandlel/2 - 32, 450, 32)
                if pushhandle_code[-2:] ==  'TP':
                    pushhandle_horizontal.setBrush(QColor('yellow'))
                else:
                    pushhandle_horizontal.setBrush(QColor('grey'))
                self.scene.addItem(pushhandle)
                self.scene.addItem(pushhandle_horizontal)
            else:
                pushhandle = QGraphicsRectItem(pushhandlex,doory/2-pushhandlel/2,32,pushhandlel)
                if pushhandle_code[-2:] ==  'TP':
                    pushhandle.setBrush(QColor('yellow'))
                else:
                    pushhandle.setBrush(QColor('grey'))
                self.scene.addItem(pushhandle)

        if pushhandlex2 != 0:
            if pushhandle_name2[2:5] == '626':
                pushhandle2 = QGraphicsRectItem(pushhandlex2, doory/2-pushhandlel2/2,32,pushhandlel2)
                pushhandle2_horizontal = QGraphicsRectItem(pushhandlex2, doory/2 + pushhandlel2/2 - 32, 450, 32)
                if pushhandle_code2[-2:] ==  'TP':
                    pushhandle2_horizontal.setBrush(QColor('yellow'))
                else:
                    pushhandle2_horizontal.setBrush(QColor('grey'))
                self.scene.addItem(pushhandle2)
                self.scene.addItem(pushhandle2_horizontal)
            else:
                pushhandle2 = QGraphicsRectItem(pushhandlex2, doory/2 -
                pushhandlel2/2,32,pushhandlel2)
                if pushhandle_code2[-2:] ==  'TP':
                    pushhandle2.setBrush(QColor('yellow'))
                else:
                    pushhandle2.setBrush(QColor('grey'))
                self.scene.addItem(pushhandle2)
        if knob_code !='none' and knob_code !='None':
            if sidedoor == 'правая' and doorx2 == 0:
                knob = QGraphicsRectItem(68,1000, 32,32)
            else:
                knob = QGraphicsRectItem(doorx - 132,doory/2, 32,32)
            if knob_code[-2:] == 'TP':
                knob.setBrush(QColor('yellow'))
            else:
                knob.setBrush(QColor('grey'))
            self.scene.addItem(knob)
        if knob_code2 !='none' and knob_code2 !='None':
            knob2 = QGraphicsRectItem(1068,1000, 32,32)
            if knob_code2[-2:] == 'TP':
                knob2.setBrush(QColor('yellow'))
            else:
                knob2.setBrush(QColor('grey'))
            self.scene.addItem(knob2)

        if doorlockx != 0:
            doorlock = QGraphicsRectItem(doorlockx,doorlocky,doorlockw,doorlockl)
            if doorlock_code[-2:] == 'TP':
                doorlock.setBrush(QColor('yellow'))
            else:
                doorlock.setBrush(QColor('grey'))
            self.scene.addItem(doorlock)

        if doorlockx2 != 0:
            doorlock2 = QGraphicsRectItem(doorlockx2,doorlocky2,
                                          doorlockw2,doorlockl2)
            if doorlock_code2[-2:] == 'TP':
                doorlock2.setBrush(QColor('yellow'))
            else:
                doorlock2.setBrush(QColor('grey'))
            self.scene.addItem(doorlock2)
        if lefProfL != 0:
            #if upy == 0:
            left_prof = QGraphicsRectItem(0-leftx, 0-upy-zazor2, 35, lefProfL)
            #left_prof.setBrush(QColor('grey'))
            self.scene.addItem(left_prof)
        if RProfL != 0:
            #if upy == 0:
            right_prof = QGraphicsRectItem(0+doorx+doorx2+rightx-35+5+zazorx,
                                           0-upy-zazor2, 35, RProfL)
            #left_prof.setBrush(QColor('grey'))
            self.scene.addItem(right_prof)

        if leftCapL != 0:
            left_cap = QGraphicsRectItem(0-leftx, 0-upy-zazor2, 40, leftCapL)
            if leftCapN[6:8] == 'ТР':
                left_cap.setBrush(QColor('yellow'))
            else:
                left_cap.setBrush(QColor('grey'))
            self.scene.addItem(left_cap)

        if rightCapL != 0:
            right_cap = QGraphicsRectItem(0+doorx+doorx2+rightx-40+5+zazorx, 0 -
                                          upy-zazor2, 40, rightCapL)
            if rightCapN[6:8] == 'ТР':
                right_cap.setBrush(QColor('yellow'))
            else:
                right_cap.setBrush(QColor('grey'))
            self.scene.addItem(right_cap)
        if upProfN != 'none':
            if upx != 0:
                upProf = QGraphicsRectItem(0-leftx, 0-upy-zazor2, upx+
                                           leftx + rightx, 35)
            elif upx == 0 and leftx == 0 and rightx !=0:
                upProf = QGraphicsRectItem(0+doorx+doorx2 + 5 + zazorx, 0 -
                                           upy-zazor2, upx+
                                           leftx + rightx, 35)
            elif upx == 0 and leftx != 0 and rightx == 0:
                upProf = QGraphicsRectItem(0 - leftx - 5, 0 - upy-zazor2 , upx +
                                           leftx + rightx, 35)
            elif upx == 0 and leftx != 0 and rightx == 0:
                upProf = QGraphicsRectItem(0 - leftx - 5, 0 - upy-zazor2 , upx +
                                           leftx + rightx, 35)
            elif upx == 0 and leftx != 0 and rightx != 0:
                upProf = QGraphicsRectItem(0 - leftx - 5, 0 - upy-zazor2,
                                           leftx, 35)
                upProf2 = QGraphicsRectItem(0+doorx+doorx2 + 5 + zazorx, 0 -
                                            upy-zazor2, leftx, 35)
                self.scene.addItem(upProf2)
            self.scene.addItem(upProf)
        if upCapN != 'none':
            if upx != 0:
                upCap = QGraphicsRectItem(0-leftx, 0-upy-zazor2, upx+
                                           leftx + rightx, 40)
            elif upx == 0 and leftx == 0 and rightx !=0:
                upCap = QGraphicsRectItem(0+doorx+doorx2 + 5 + zazorx, 0 -
                                           upy-zazor2, upx+
                                           leftx + rightx, 40)
            elif upx == 0 and leftx != 0 and rightx == 0:
                upCap = QGraphicsRectItem(0 - leftx - 5, 0 - upy-zazor2 , upx +
                                           leftx + rightx, 40)
            elif upx == 0 and leftx != 0 and rightx == 0:
                upCap = QGraphicsRectItem(0 - leftx - 5, 0 - upy-zazor2 , upx +
                                           leftx + rightx, 40)
            elif upx == 0 and leftx != 0 and rightx != 0:
                upCap = QGraphicsRectItem(0 - leftx - 5, 0 - upy-zazor2,
                                           leftx, 40)
                upCap2 = QGraphicsRectItem(0+doorx+doorx2 + 5 + zazorx, 0 -
                                            upy-zazor2, leftx, 40)
                if upCapN[6:8] == 'ТР':
                    upCap2.setBrush(QColor('yellow'))
                else:
                    upCap2.setBrush(QColor('grey'))
                self.scene.addItem(upCap2)
            if upCapN[6:8] == 'ТР':
                upCap.setBrush(QColor('yellow'))
            else:
                upCap.setBrush(QColor('grey'))
            self.scene.addItem(upCap)
        if downProfN != 'none':
            if leftx == 0 and rightx != 0:
                downPr = QGraphicsRectItem(0+doorx+doorx2 + 5 + zazorx, righty -
                                           35, rightx, 35)
            elif leftx != 0 and rightx == 0:
                downPr = QGraphicsRectItem(0 - leftx - 5, lefty - 35, leftx, 35)
            else:
                downPr = QGraphicsRectItem(0 - leftx - 5, lefty - 35, leftx, 35)
                downPr2 = QGraphicsRectItem(0 + doorx + doorx2 + 5 + zazorx,
                                            righty - 35, rightx, 35)
                self.scene.addItem(downPr2)
            self.scene.addItem(downPr)

        if downCapN != 'none':
            if leftx == 0 and rightx != 0:
                downCap = QGraphicsRectItem(0+doorx+doorx2 + 5 + zazorx, righty -
                                           40, rightx, 40)
            elif leftx != 0 and rightx == 0:
                downCap = QGraphicsRectItem(0 - leftx - 5, lefty - 40, leftx, 40)
            else:
                downCap = QGraphicsRectItem(0 - leftx - 5, lefty - 40, leftx, 40)
                downCap2 = QGraphicsRectItem(0 + doorx + doorx2 + 5 + zazorx,
                                            righty - 40, rightx, 40)
                if downCapN[6:8] == 'ТР':
                    downCap2.setBrush(QColor('yellow'))
                else:
                    downCap2.setBrush(QColor('grey'))
                self.scene.addItem(downCap2)
            if downCapN[6:8] == 'ТР':
                downCap.setBrush(QColor('yellow'))
            else:
                downCap.setBrush(QColor('grey'))
            self.scene.addItem(downCap)

        self.graphicsView.show()
