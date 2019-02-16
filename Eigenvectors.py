# Chris Nelson 2018
# Program for graphing eigenvectors for linear algebra project
# originally written in codeskulptor (py3.codeskulptor.org)
# link to project can be found at: https://goo.gl/sa1Mvt

import simplegui
import random

#canvas variables
c_width = 1000
c_height = 800

origin = [(c_width/2), (c_height/2)]

#keeps tracks of num of points drawn
pointCounter = 0

#converst normal coordinate values into python axis such that the origin is in the middle of the canvas
def pyify(x,y):
    return [int(origin[0]+ x), int(origin[1] - y)]

##############################################

def randX():
    return random.randint(int(-0.4*c_width),int(0.4*c_width))
def randY():
    return random.randint(-0.4*c_height, 0.4*c_height)

def matrixX(x,y):
    return 0.45*x + 0.54*y
def matrixY(x,y):
    return -0.2*x + 1.3*y
def varInit():
    global x0, y0, a0,b0,c0,d0,e0,f0, lineList1, lineList2, lineList3, lineList4
    x0 =randX()
    y0 = randY()
    a0 =randX()
    b0 =randY()
    c0 =randX()
    d0 =randY()
    e0 =randX()
    f0 =randY()
    lineList1 = [pyify(x0, y0)]
    lineList2 = [pyify(a0, b0)]
    lineList3 = [pyify(c0, d0)]
    lineList4 = [pyify(e0, f0)]

varInit()
def click():
    global pointCounter, lineList1, lineList2, lineList3, lineList4
    pointCounter = 0
    varInit()



# Handler to draw on canvas
def draw(canvas):
    global x0, y0, a0,b0,c0,d0,e0,f0, pointCounter
    if(pointCounter<50):
        ##multiply prevous point by matrix
        x = matrixX(x0, y0)
        y = matrixY(x0, y0)
        a = matrixX(a0, b0)
        b = matrixY(a0, b0)
        c = matrixX(c0, d0)
        d = matrixY(c0, d0)
        e = matrixX(e0, f0)
        f = matrixY(e0, f0)


        ##append points
        lineList1.append(pyify(x,y))
        lineList2.append(pyify(a,b))
        lineList3.append(pyify(c,d))
        lineList4.append(pyify(e,f))
        pointCounter+=1

        #assigning x(k) to x(k+1) for next time through
        y0=y
        x0=x
        a0=a
        b0=b
        c0=c
        d0=d
        e0=e
        f0=f


    #axes
    canvas.draw_line((0, c_height/2), (c_width, c_height/2), 1, "black")
    canvas.draw_line((c_width/2, 0), (c_width/2, c_height), 1, "black")

    #dividing unit marker x
    canvas.draw_line((c_width/4, c_height/2 +5), (c_width/4, c_height/2 -5), 1, "black")
    canvas.draw_line((c_width*3/4, c_height/2 +5), (c_width*3/4, c_height/2 -5), 1, "black")
    canvas.draw_text(str(int(c_width/-4)), (c_width/4-12, c_height/2+17), 11, "black")
    canvas.draw_text(str(int(c_width/4)), (c_width*3/4-8, c_height/2+17), 11, "black")

    #dividing unit marker y
    canvas.draw_line((c_width/2-5, c_height/4), (c_width/2+5, c_height/4), 1, "black")
    canvas.draw_line((c_width/2-5, c_height*3/4), (c_width/2+5, c_height*3/4), 1, "black")
    canvas.draw_text(str(int(c_height/4)), (c_width/2-25, c_height/4+3), 11, "black")
    canvas.draw_text(str(int(c_height/-4)), (c_width/2-30, c_height*3/4+4), 11, "black")

    #eigenvector 1
    v1L = 0.25*c_width
    canvas.draw_line( (pyify(-1*v1L, -1.2861*v1L)), (pyify(v1L,1.2861*v1L)) , 1.2, "Grey")
    canvas.draw_text("V1",(pyify(v1L+5,1.2861*v1L+6)) , 11, "grey")

    #eigenvector 2
    v2L = 0.4*c_width
    canvas.draw_line( (pyify(-1*v2L, -0.288*v2L)), (pyify(v2L,0.288*v2L)) , 1.2, "Grey")
    canvas.draw_text("V2",(pyify(v2L+6,0.288*v2L)) , 11, "grey")

    #matrix lines
    canvas.draw_polyline(lineList1, 3, "blue")
    canvas.draw_circle(lineList1[0], 2, 3, "blue")
    canvas.draw_text("x1", (lineList1[0][0], lineList1[0][1]+20), 12, "blue")

    canvas.draw_polyline(lineList2, 3, "red")
    canvas.draw_circle(lineList2[0], 2, 3, "red")
    canvas.draw_text("x2", (lineList2[0][0], lineList2[0][1]+20), 12, "red")

    canvas.draw_polyline(lineList3, 3, "green")
    canvas.draw_circle(lineList3[0], 2, 3, "green")
    canvas.draw_text("x3", (lineList3[0][0], lineList3[0][1]+20), 12, "green")

    canvas.draw_polyline(lineList4, 3, "orange")
    canvas.draw_circle(lineList4[0], 2, 3, "orange")
    canvas.draw_text("x4", (lineList4[0][0], lineList4[0][1]+20), 12, "orange")


    pt1 = ("x1= "+str([int(lineList1[0][0]-c_width/2), int(c_height/2-lineList1[0][1])]))
    pt2 = ("x2= "+str([int(lineList2[0][0]-c_width/2), int(c_height/2-lineList2[0][1])]))
    pt3 = ("x3= "+str([int(lineList3[0][0]-c_width/2), int(c_height/2-lineList3[0][1])]))
    pt4 = ("x4= "+str([int(lineList4[0][0]-c_width/2), int(c_height/2-lineList4[0][1])]))


    canvas.draw_text(  pt1 , (20, 30), 15, "black")
    canvas.draw_text(  pt2 , (20, 50), 15, "black")
    canvas.draw_text(  pt3 , (20, 70), 15, "black")
    canvas.draw_text(  pt4 , (20, 90), 15, "black")







# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Eigen Value Grapher", c_width, c_height)
frame.set_canvas_background('White')
frame.set_draw_handler(draw)
frame.add_button("Regenerate", click)

# Start the frame animation
frame.start()
