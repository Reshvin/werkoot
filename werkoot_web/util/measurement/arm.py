from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import math
import cv2

# cardCnt = None
# pixelsPerMetric = None
# y_values = None

def edge(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    bilat = cv2.bilateralFilter(gray, 11, 17, 17)
    canny = cv2.Canny(bilat, 30, 200)
    return canny

def midpoint(ptA, ptB):
    return((ptA[0] + ptB[0])*0.5, (ptA[1]+ptB[1])*0.5)


def measure(image):
        image = imutils.resize(image, height = 300)

        edged = edge(image)
        # cv2.imshow('edge', edged)

        cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]

        for c in cnts:
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.015 * peri, True)

                if len(approx) == 4:
                        cardCnt = approx
                        break

        try:
                box = cv2.minAreaRect(cardCnt)
                box = cv2.boxPoints(box)
                box = np.array(box, dtype='int')
                box = perspective.order_points(box)

                (tl,tr,br,bl) = box

                (tmidX, tmidY) = midpoint(tl,tr)
                (bmidX, bmidY) = midpoint(bl,br)
                (lmidX, lmidY) = midpoint(tl,bl)
                (rmidX, rmidY) = midpoint(tr,br)

                # cv2.line(image, (int(tmidX),int(tmidY)),(int(bmidX),int(bmidY)), (255,255,0), 1)
                # cv2.line(image, (int(lmidX),int(lmidY)),(int(rmidX),int(rmidY)), (255,255,0), 1)

                dA = dist.euclidean((tmidX,tmidY),(bmidX,bmidY))
                dB = dist.euclidean((lmidX,lmidY),(rmidX,rmidY))

                pixelsPerMetric = dA / 53.98

                dimA = dA/pixelsPerMetric
                dimB = dB/pixelsPerMetric

                # cv2.putText(image, "{:.1f}mm".format(dimA),(int(tmidX-10),int(tmidY-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
                # cv2.putText(image, "{:.1f}mm".format(dimB),(int(rmidX+10),int(rmidY)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)

                # cv2.drawContours(image, [cardCnt], -1, (0, 255, 255), 2)

                left = lmidX - 5
                right = rmidX + 5
                top = tmidY - (int(50 * pixelsPerMetric))
                bottom = bmidY + (int(50 * pixelsPerMetric))


                polygons = np.array([[(left, top), (right, top), (right, bottom), (left, bottom)]], 'int32')
                mask = np.zeros_like(edged)
                cv2.fillPoly(mask, polygons, 255)
                masked_image = cv2.bitwise_and(edged,mask)
                # cv2.imshow('mask', masked_image)

                lines = cv2.HoughLinesP(masked_image, 1, np.pi/180, 5, np.array([]), minLineLength=5, maxLineGap=10)

                max_y = 0
                min_y = 1000
                for line in lines:
                        for points in line:
                                x1, y1, x2, y2 = points
                                if y1 > max_y:
                                        max_y = y1
                                
                                if y1 < min_y:
                                        min_y = y1
                                
                                if y2 > max_y:
                                        max_y = y2
                                
                                if y2 < min_y:
                                        min_y = y2

                y_dist = max_y - min_y
                diameter = y_dist / pixelsPerMetric
                circ = math.pi*diameter
                circ = circ - 40
                return int(circ)

        except:
                return None


        # cv2.imshow("result", image)
        # cv2.waitKey(0)


# image = cv2.imread('IMG_1249.jpg')
# measure(image)