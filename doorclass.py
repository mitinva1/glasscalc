# -*- coding: utf-8 -*-
class ListInstance:
    def __str__(self):
        """return '<Instance of %s, address %s:\n%s>' %(
            self.__class__.__name__,
            id(self), self.__attrnames())"""
        return self.__attrnames()
    """def __attrnames(self):
        result =''
        for attr in sorted(self.__dict__):
            result+='\tname %s=%s\n' %(attr, self.__dict__[attr])
        return result"""
    def __attrnames(self):
        result =''
        for attr in sorted(self.__dict__):
            if (attr[-4:] == 'name' and self.__dict__[attr] != 'none' and
                    self.__dict__[attr] != 'New Door' or attr[-5:] == 'name2'
                    and self.__dict__[attr] != 'none'
                    and self.__dict__[attr] != 'New Door'):
                result += (self.__dict__[attr] + '\n')
        return result

class Fittings(ListInstance):#основной класс для фурнитуры
    def __init__(self, code, name='none', colour='none', price=0):
        self.code=code
        self.name= name
        self.colour=colour
        self.price=price
    def order(self):
        print(self.name, 'in standart fittings')
    def __repr__(self): #класс который выводит инфу ниже через print
        return "<Фурнитура: артикул=%s, цена=%s>" % (self.name, self.price)

class BottomFitting(Fittings):#нижний фитинг
    def __init__(self, code, name='none', colour='none', price=0):
        Fittings.__init__(self, code, name, colour, price)
    def work(self):
        print(self.name, 'is a BottomFitting for glass door')

class TopFitting(Fittings):#верхний фитинг
    def __init__(self, code, name='none', colour='none', price=0):
        Fittings.__init__(self, code, name, colour, price)
    def work(self):
        print(self.name, 'is a TopFitting for glass door')

class SupportTopFitting(Fittings):#нижняя ось или доводчик
    def __init__(self, code, name='none', colour='none', price=0):
        Fittings.__init__(self, code, name, colour, price)
    def work(self):
        print(self.name, 'is a SupportTopFitting for glass door')

class SupportBF(Fittings):#верхняя ось
    def __init__(self, code, name='none', colour='none', price=0):
        Fittings.__init__(self, code, name, colour, price)
    def work(self):
        print(self.name, 'is a SupportBottomFitting for glass door')

class Hinge(Fittings):#Петля боковая
    def __init__(self, code, name='none', colour='none', price=0, pcs=0):
        Fittings.__init__(self, code, name, colour, price)
        self.pcs=pcs
    def work(self):
        print(self.name, 'is a Hinge for glass door')

class DoorHandle(Fittings):#нажимной гарнитур
    def __init__(self, code, name='none', colour='none', price=0):
        Fittings.__init__(self, code, name, colour, price)
    def work(self):
        print(self.name, 'is a DoorHandle for glass door')

class PushHandle(Fittings):#офисная рука
    def __init__(self, code, name='none', colour='none', price=0, length='0'):
        Fittings.__init__(self, code, name, colour, price)
        self.length=length
    def work(self):
        print(self.name, 'is a PushHandle for glass door')
class knob(Fittings):#замокыфв
    def __init__(self, code, name='none', colour='none',
                 price = 0, id_knob = 0):
        Fittings.__init__(self, code, name, colour, price)
        self.id_knob = id_knob
    def work(self):
        print(self.name, 'is a knob')

class DoorLock(Fittings):#замок
    def __init__(self, code, name='none', colour='none', price=0):
        Fittings.__init__(self, code, name, colour, price)
    def work(self):
        print(self.name, 'is a DoorLock for glass door')

class DoorLock(Fittings):#замок
    def __init__(self, code, name='none', colour='none', price=0):
        Fittings.__init__(self, code, name, colour, price)
    def work(self):
        print(self.name, 'is a DoorLock for glass door')

class MateDoorLock(Fittings):#замок
    def __init__(self, code, name='none', colour='none', price=0):
        Fittings.__init__(self, code, name, colour, price)
    def work(self):
        print(self.name, 'is a DoorLock for glass door')

class Compactor(Fittings):#замокыфв
    def __init__(self, code, name='none', colour='none', price=0):
        Fittings.__init__(self, code, name, colour, price)
    def work(self):
        print(self.name, 'is a DoorLock for glass door')


class Glass(ListInstance):
    def __init__(self, code, name='none', colour='none', price=0):
        self.code=code
        self.name= name
        self.colour=colour
        self.price=price

class UpGlass(ListInstance):
    def __init__(self, code, name='none', colour='none',
                 price=0, height=0, width=0,
                 upx=0, upy=0):
        self.code = code
        self.name = name
        self.colour = colour
        self.price = price
        self.height = height
        self.width =  width
        self.upx = upx
        self.upy = upy
    def area(self):
        return self.height*self.width/1000000
    def work(self):
        print(self.name, 'верхнее стекло')
    def priceup(self):
        return (self.height*self.width/1000000*self.price)
    def for_scene(self):
        return (self.width, self.height)

class Door(ListInstance):
    def __init__(
            self, name, quantitydoor=1, sidedoor="правая",
            glassname='None', glass_colour='None',
            doorx=1000, doory=2000,
            doorx2=0, doory2=0,
            doorglassprice=0,
            botfit_name='None', botfit_colour='None',
            botfitx=0, botfitprice=0,
            botfit_name2='None', botfit_colour2 = 'None', botfitx2 = 0,
            botfitprice2 = 0, botfit_base = 'BottomFitting',
            supportbf_name = 'None', supportbf_colour = 'None',
            supportbf_x = 0,
            supportbf_w = 0, supportbf_l = 0, supportbf_price = 0,
            supportbf_name2 = 'None', supportbf_colour2 = 'None',
            supportbf_x2 = 0,
            supportbf_w2 = 0, supportbf_l2 = 0, supportbf_price2 = 0,
            topfit_name = 'None', topfit_colour = 'None',
            topfitx = 0,topfitprice = 0,
            topfit_name2 = 'None', topfit_colour2 = 'None',
            topfitx2 = 0,topfitprice2 = 0,
            supporttf_name = 'None', supporttf_colour = 'None',
            supporttf_x = 0,
            supporttf_w = 0, supporttf_l = 0, supporttf_price = 0,
            supporttf_name2 = 'None', supporttf_colour2 = 'None',
            supporttf_x2 = 0,
            supporttf_w2 = 0, supporttf_l2 = 0, supporttf_price2 = 0,
            hinge_code = 'None',
            hinge_name = 'None', hinge_quantity = 2, hinge_x = 0,
            hinge_price = 0,
            hinge_code2 = 'None',
            hinge_name2 = 'None', hinge_x2 = 0, hinge_price2 = 0,
            doorhandle_code = 'None',
            doorhandle_name = 'None', doorhandle_x = 0, doorhandle_x2 = 0,
            doorhandle_price = 0,
            doorhandle_code2='None',
            doorhandle_name2 = 'None', doorhandle_x_2 = 0,
            doorhandle_x2_2 = 0,
            doorhandle_price2 = 0, pushhandle_code='none',
            pushhandle_name = 'None', pushhandle_x = 0,
            pushhandle_l = 0, pushhandle_price = 0,
            pushhandle_code2='none',
            pushhandle_name2 = 'None', pushhandle_x2 = 0,
            pushhandle_l2 = 0, pushhandle_price2 = 0, knob_code = 'None',
            knob_name='none', knob_x=0, knob_price=0, knob_code2='None',
            knob_name2 = 'none', knob_x2 = 0, knob_price2 = 0,
            doorlock_code='none', doorlock_name = 'None',
            doorlock_x = 0, doorlock_y = 0,
            doorlock_w = 0,doorlock_l = 0, doorlock_y2 = 'н', doorlock_price = 0, doorlock_code2='none',
            doorlock_name2 = 'None',
            doorlock_x2 = 0, doorlock_y_2 = 0,
            doorlock_w2 = 0,doorlock_l2 = 0, doorlock_y2_2 = 'н', doorlock_price2 = 0,
            matedoorlock_name = 'None', matedoorlock_price = 0,
            matedoorlock_name2 = 'None', matedoorlock_price2 = 0,
            compactor_down_name = 'none', compactor_down_price = 0,
            compactor_down_name2 = 'none', compactor_down_price2 = 0,
            compactor_side_name = 'none', compactor_side_price = 0,
            compactor_side_name2 = 'none', compactor_side_price2 = 0,
            compactor_up_name = 'none', compactor_up_price = 0,
            compactor_up_name2 = 'none', compactor_up_price2 = 0,
            compactor_hinge_name = 'none', compactor_hinge_price = 0,
            compactor_hinge_name2 = 'none', compactor_hinge_price2 = 0,
            price = 0, left_profile_name = 'none', left_profile_length=0,
            left_profile_price=0, right_profile_name = 'none',
            right_profile_length=0, right_profile_price=0,
            leftCap_name = 'none', leftCap_price=0, leftCap_length=0,
            rightCap_name = 'none', rightCap_price=0, rightCap_length=0,
            upProfile_name = 'none', upProfile_price=0, upProfile_length=0,
            upCap_name = 'none', upCap_price=0, upCap_length=0,
            downProfile_name = 'none', downProfile_price=0, downProfile_length=0,
            downCap_name = 'none', downCap_price=0, downCap_length=0):
        self.name = name
        self.quantitydoor = quantitydoor
        self.sidedoor = sidedoor
        self.glassname = glassname
        self.glass_colour = glass_colour
        self.doorx = doorx#in newScene
        self.doory = doory#in newScene
        self.doorx2 = doorx2
        self.doory2 = doory2
        self.doorglassprice = doorglassprice
        self.botfit_name = botfit_name
        self.botfit_colour = botfit_colour
        self.botfitx = botfitx#in newScene
        self.botfitprice = botfitprice
        self.botfit_name2 = botfit_name2
        self.botfit_colour2 = botfit_colour2
        self.botfitx2 = botfitx2
        self.botfitprice2 = botfitprice2
        self.botfit_base = botfit_base
        self.supportbf_name = supportbf_name
        self.supportbf_colour = supportbf_colour
        self.supportbf_x = supportbf_x
        self.supportbf_w = supportbf_w
        self.supportbf_l = supportbf_l
        self.supportbf_price = supportbf_price
        self.supportbf_name2 = supportbf_name2
        self.supportbf_colour2 = supportbf_colour2
        self.supportbf_x2 = supportbf_x2
        self.supportbf_w2 = supportbf_w2
        self.supportbf_l2 = supportbf_l2
        self.supportbf_price2 = supportbf_price2
        self.topfit_name = topfit_name
        self.topfit_colour = topfit_colour
        self.topfitx = topfitx#in newScene
        self.topfitprice = topfitprice
        self.topfit_name2 = topfit_name2
        self.topfit_colour2 = topfit_colour2
        self.topfitx2 = topfitx2#in newScene
        self.topfitprice2 = topfitprice2
        self.supporttf_name = supporttf_name
        self.supporttf_colour = supporttf_colour
        self.supporttf_x = supporttf_x
        self.supporttf_w = supporttf_w
        self.supporttf_l = supporttf_l
        self.supporttf_price = supporttf_price
        self.supporttf_name2 = supporttf_name2
        self.supporttf_colour2 = supporttf_colour2
        self.supporttf_x2 = supporttf_x2
        self.supporttf_w2 = supporttf_w2
        self.supporttf_l2 = supporttf_l2
        self.supporttf_price2 = supporttf_price2
        self.hinge_code = hinge_code
        self.hinge_name = hinge_name
        self.hinge_quantity = hinge_quantity
        self.hinge_x = hinge_x
        self.hinge_price = hinge_price
        self.hinge_code2 = hinge_code2
        self.hinge_name2 = hinge_name2
        self.hinge_x2 = hinge_x2
        self.hinge_price2 = hinge_price2
        self.doorhandle_code = doorhandle_code
        self.doorhandle_name = doorhandle_name
        self.doorhandle_x = doorhandle_x
        self.doorhandle_x2 = doorhandle_x2
        self.doorhandle_price = doorhandle_price
        self.doorhandle_code2 = doorhandle_code2
        self.doorhandle_name2 = doorhandle_name2
        self.doorhandle_x_2 = doorhandle_x_2
        self.doorhandle_x2_2 = doorhandle_x2_2
        self.doorhandle_price2 = doorhandle_price2
        self.pushhandle_code = pushhandle_code
        self.pushhandle_name = pushhandle_name
        self.pushhandle_x = pushhandle_x
        self.pushhandle_l = pushhandle_l
        self.pushhandle_price = pushhandle_price
        self.pushhandle_code2 = pushhandle_code2
        self.pushhandle_name2 = pushhandle_name2
        self.pushhandle_x2 = pushhandle_x2
        self.pushhandle_l2 = pushhandle_l2
        self.pushhandle_price2 = pushhandle_price2
        self.knob_code = knob_code
        self.knob_name = knob_name
        self.knob_x = knob_x
        self.knob_price = knob_price
        self.knob_code2 = knob_code2
        self.knob_name2 = knob_name2
        self.knob_x2 = knob_x2
        self.knob_price2 = knob_price2
        self.doorlock_code = doorlock_code
        self.doorlock_name = doorlock_name
        self.doorlock_x = doorlock_x
        self.doorlock_y = doorlock_y
        self.doorlock_w = doorlock_w
        self.doorlock_l = doorlock_l
        self.doorlock_y2 = doorlock_y2
        self.doorlock_price = doorlock_price
        self.doorlock_code2 = doorlock_code2
        self.doorlock_name2 = doorlock_name2
        self.doorlock_x2 = doorlock_x2
        self.doorlock_y_2 = doorlock_y_2
        self.doorlock_w2 = doorlock_w2
        self.doorlock_l2 = doorlock_l2
        self.doorlock_y2_2 = doorlock_y2_2
        self.doorlock_price2 = doorlock_price2
        self.matedoorlock_name = matedoorlock_name
        self.matedoorlock_price = matedoorlock_price
        self.matedoorlock_name2 = matedoorlock_name2
        self.matedoorlock_price2 = matedoorlock_price2
        self.compactor_down_name  = compactor_down_name
        self.compactor_down_price = compactor_down_price
        self.compactor_down_name2  = compactor_down_name2
        self.compactor_down_price2 = compactor_down_price2
        self.compactor_side_name  = compactor_side_name
        self.compactor_side_price = compactor_side_price
        self.compactor_side_name2  = compactor_side_name
        self.compactor_side_price2 = compactor_side_price
        self.compactor_up_name  = compactor_up_name
        self.compactor_up_price = compactor_up_price
        self.compactor_up_name2  = compactor_up_name
        self.compactor_up_price2 = compactor_up_price
        self.compactor_hinge_name  = compactor_hinge_name
        self.compactor_hinge_price = compactor_hinge_price
        self.compactor_hinge_name2  = compactor_hinge_name
        self.compactor_hinge_price2 = compactor_hinge_price
        self.price = price
        self.knob_code = knob_code
        self.knob_name = knob_name
        self.knob_price = knob_price
        self.knob_code2 = knob_code2
        self.knob_name2 = knob_name2
        self.knob_price2 = knob_price2
        self.left_profile_name = left_profile_name
        self.left_profile_length = left_profile_length
        self.left_profile_price = left_profile_price
        self.right_profile_name = right_profile_name
        self.right_profile_length = right_profile_length
        self.right_profile_price = right_profile_price
        self.leftCap_name = leftCap_name
        self.leftCap_price = leftCap_price
        self.leftCap_length = leftCap_length
        self.rightCap_name = rightCap_name
        self.rightCap_price = rightCap_price
        self.rightCap_length = rightCap_length
        self.upProfile_name = upProfile_name
        self.upProfile_price = upProfile_price
        self.upProfile_length = upProfile_length
        self.upCap_name = upCap_name
        self.upCap_price = upCap_price
        self.upCap_length = upCap_length
        self.downProfile_name = downProfile_name
        self.downProfile_price = downProfile_price
        self.downProfile_length = downProfile_length
        self.downCap_name = downCap_name
        self.downCap_price = downCap_price
        self.downCap_length = downCap_length
    def doorPrice(self):
        return (self.doorglassprice + self.botfitprice +
                self.botfitprice2 + self.supportbf_price +
                self.supportbf_price2 + self.topfitprice +
                self.topfitprice2 + self.supporttf_price +
                self.supporttf_price2 + (self.hinge_price*
                self.hinge_quantity) + (self.hinge_quantity *
                self.hinge_price2) + self.doorhandle_price +
                self.doorhandle_price2 + self.pushhandle_price +
                self.pushhandle_price2 + self.doorlock_price +
                self.doorlock_price2 + self.matedoorlock_price +
                self.matedoorlock_price2 + self.compactor_down_price +
                self.compactor_down_price2 + self.compactor_side_price + self.compactor_side_price2 + self.compactor_up_price +
                self.compactor_up_price2 + self.compactor_hinge_price +
                self.compactor_hinge_price2 + self.knob_price +
                self.knob_price2 + self.left_profile_price +
                self.right_profile_price + self.leftCap_price +
                self.rightCap_price + self.upProfile_price +
                self.upCap_price + self.downCap_price + self.downProfile_price)
    def accessories(self):
        result = """"""
        for attr in sorted(self.__dict__):
            if (attr[-4:] == 'name' and self.__dict__[attr] != 'none' and
                    self.__dict__[attr] != 'New Door' or attr[-5:] == 'name2'
                    and self.__dict__[attr] != 'none'
                    and self.__dict__[attr] != 'New Door'):
                result += '%s. '%(self.__dict__[attr])
        return result
    def for_scene(self):
        result2 = (self.glass_colour,
                   self.doorx, self.doory, self.doorx2, self.doory2, self.sidedoor,
                   self.botfitx,
                   self.botfit_colour, self.botfit_colour2,
                   self.botfitx2,
                   self.supportbf_x, self.supportbf_w,
                   self.supportbf_l,
                   self.supportbf_colour,
                   self.supportbf_x2, self.supportbf_w2,
                   self.supportbf_l2,
                   self.supportbf_colour2,
                   self.topfitx, self.topfit_colour,
                   self.topfitx2, self.topfit_colour2,
                   self.supporttf_x, self.supporttf_w,
                   self.supporttf_l,
                   self.supporttf_colour,
                   self.supporttf_x2, self.supporttf_w2,
                   self.supporttf_l2,
                   self.supporttf_colour2,
                   self.hinge_code, self.hinge_code2,
                   self.hinge_x, self.hinge_x2, self.hinge_quantity,
                   self.doorhandle_code,
                   self.doorhandle_x, self.doorhandle_x2,
                   self.doorhandle_code2,
                   self.doorhandle_x_2, self.doorhandle_x2_2,
                   self.pushhandle_code, self.pushhandle_name,
                   self.pushhandle_x, self.pushhandle_l,
                   self.pushhandle_code, self.pushhandle_name2,
                   self.pushhandle_x2, self.pushhandle_l2,
                   self.doorlock_code, self.doorlock_x,
                   self.doorlock_y, self.doorlock_w,
                   self.doorlock_l, self.doorlock_code2,
                   self.doorlock_x2, self.doorlock_y_2,
                   self.doorlock_w2, self.doorlock_l2, self.knob_code,
                   self.knob_code2)# self.left_profile_length)
        return result2
    def for_scene2(self):
        result3 = (self.left_profile_length, self.right_profile_length,
                   self.leftCap_length, self.leftCap_name,
                   self.rightCap_length, self.rightCap_name,
                   self.upProfile_name, self.upCap_name, self.downProfile_name,
                   self.downCap_name)
        return result3
class GlazingProfile(ListInstance):
    def __init__(self, code='none', name='none',
                 colour='none', price=0, length=0,
                 length_real=0, side='none'):
        self.code = code
        self.name = name
        self.colour = colour
        self.price = price
        self.length = length
        self.length_real = length_real
        self.side = side
    def priceup(self):
        return self.price

class GlazingCap(ListInstance):
    def __init__(self, code, name='none', colour='none',
                 price=0, length=0, length_real=0, side='none'):
        self.code = code
        self.name = name
        self.colour = colour
        self.price = price
        self.length = length
        self.length_real = length_real
        self.side = side
    #def quantity1(self):#quantity profile/3000
    #    l_prof = float(self.length)
    #    quantity2 = self.length_real%l_prof
    #    if quantity2 != 0:
    #        quantity2 = (quantity2+(l_prof-quantity2%
    #        self.length))/self.length
    #    else:
    #        quantity2 = self.length_real%self.length
    #    return quantity2
    #def dd(a,b,c,d):
	#	 ss=a+b+c+d
	#	 ww=ss%3000
	#	 if ww != 0:
	#	     qa=ss//3000 + 1
	#	 else:
	#	     qa=ss/3000
	#	 return qa
    def priceup(self):
        return self.price

    #def quantity(self):
    #    if return prof


#upProfile = GlazingProfile('none')
#leftProfile = GlazingProfile('none')
#rightProfile = GlazingProfile('none')
#downProfile = GlazingProfile('none')
#upCap = doorclass.GlazingCap('none') 'верх без'
#leftCap = doorclass.GlazingCap('none') 'лев без'
#rightCap = doorclass.GlazingCap('none') 'прав. без'
#downCap = doorclass.GlazingCap('none') 'низ без'

if __name__ == '__main__':
    t301sss = Hinge('T301SSS')
    t301sss.colour = 'SSS'
    t301sss.price = 3000
    t301sss.info = 'Блок информации работает'
    glass10 = Glass('newglass')
    glass10.price = 2000
    print(glass10)
