# import the library opencv
import random
import cv2
import imutils
# globbing utility.
import glob

# img = cv2.imread("E:/Company Work/Artifical Inteligence task/Kiran/image_shapes.png", cv2.IMREAD_GRAYSCALE)
path = "E:/multiply/multiply/*.*"


#math_sym_list = [ 'Minus', 'Minus', 'Minus', 'Minus', 'Minus', 'Minus', 'Minus', 'Minus', 'Minus', 'Minus']
#math_sym_list = ['Plus', 'Plus', 'Plus', 'Plus', 'Plus', 'Plus', 'Plus', 'Plus', 'Plus', 'Plus']
math_sym_list=['Multiply', 'Multiply', 'Multiply', 'Multiply', 'Multiply', 'Multiply', 'Multiply', 'Multiply', 'Multiply', 'Multiply']
#                  'Minus', 'Minus', 'Minus', 'Minus', 'Minus', 'Minus', 'Minus', 'Minus', 'Minus', 'Minus']


# 'Plus', 'Plus', 'Plus', 'Plus', 'Plus', 'Plus', 'Plus', 'Plus', 'Plus', 'Plus'
# 'Multiply', 'Multiply', 'Multiply', 'Multiply', 'Multiply', 'Multiply', 'Multiply', 'Multiply', 'Multiply', 'Multiply',
math_img_list =[]


for file in glob.glob(path):
    img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    
    resized = imutils.resize(img, width=400)
     
    #cv2.imshow("shapes", img)
     
    _, threshold = cv2.threshold(resized, 220, 255, cv2.THRESH_BINARY)
    _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     
    font = cv2.FONT_HERSHEY_COMPLEX
     
    for cnt in contours:
        M = cv2.moments(cnt)
#         x = int((M["m10"] / M["m00"]))
#         y = int((M["m01"] / M["m00"]))
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        cv2.drawContours(resized, [cnt], 0, (0), 1)
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        print(len(approx))
   
        if len(approx) == 12:
            (x, y, w, h) = cv2.boundingRect(approx)
            print("length", x, y, w, h)
            ar = w / float(h)
            print("arc", ar)
            math_img_list.append("Plus")
            print("Symbol name = Plus, percentage = 100%")
            cv2.putText(resized, "Plus:100%", (x, y), font, 1, (0))
            

            
        elif len(approx) == 4:
            #print("Minus")
            (x, y, w, h) = cv2.boundingRect(approx)
            print("length", x, y, w, h)
            ar = w / float(h)
            print("arc", ar)
            math_img_list.append("Minus")
            
#             n = len(math_img_list)
#             m = int(n / 2)
#             minuslist = math_img_list
            
            print("Symbol name = Minus, percentage = 100%")
            cv2.putText(resized, "Minus:100%", (x, y), font, 1, (0))
             
        
        elif len(approx) == 28:
            (x, y, w, h) = cv2.boundingRect(approx)
            print("length", x, y, w, h)
            ar = w / float(h)
            print("arc", ar)
            math_img_list.append("Multiply")
            print("Symbol name = Multiply,percentage = 100%")
            cv2.putText(resized, "Multiply:100%", (x, y), font, 1, (0))
                      
 
        elif len(approx) == 6:
            #         print("Division")
            print("Symbol name = Division, percentage = 100%")
            cv2.putText(resized, "Division 100%", (x, y), font, 1, (0))

    cv2.imshow("resized", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(len(math_img_list))
    n=len(math_img_list)
#     m=int(n/2)


print("math_sym_list", math_sym_list)

#print("math_img_list", math_img_list[0:n])




def compare(a, b):
    for x, y in zip(a, b):
        if x == y:
            print("Match")
        else:
            print("No Match")


while("Minus" in math_img_list) : 
 math_img_list.remove("Minus") 
compare(math_img_list, math_sym_list)

accuracy = len([math_sym_list[i] for i in range(0, len(math_sym_list)) if math_sym_list[i] == math_img_list[i]]) / len(math_sym_list)
print(accuracy)

print("math_sym_list", math_sym_list)
print("math_img_list", math_img_list[0:n])








# # import the library opencv
# import cv2
# import imutils
# # globbing utility.
# import glob
# 
# 
# math_img_list = []
# # img = cv2.imread("E:/Company Work/Artifical Inteligence task/Kiran/image_shapes.png", cv2.IMREAD_GRAYSCALE)
# 
# # path = "E:\Company Work\Artifical Inteligence task\sym5\+\*.*"
# path = "E:/tfrecord/M/*.*"
# print("hello")
# for file in glob.glob(path):
#     print("hi")
#    
#     img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
#     resized = imutils.resize(img, width=400)
#      
# #     cv2.imshow("shapes", img) 
#      
#     _, threshold = cv2.threshold(resized, 220, 255, cv2.THRESH_BINARY)
#     _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#      
#     font = cv2.FONT_HERSHEY_COMPLEX
#      
#     for cnt in contours:
#         
#         M = cv2.moments(cnt)
#         x = int((M["m10"] / M["m00"]) )
#         y = int((M["m01"] / M["m00"]) )
#         
#         approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
#      
#         cv2.drawContours(resized, [cnt], 0, (0), 1)
# #         x = approx.ravel()[0]
# #         y = approx.ravel()[1]
#         print(len(approx))
#    
#         if len(approx) == 12:
#             print("Symbol name = plus, percentage = 100%")
#             #         print("plus")
#             cv2.putText(resized, "plus 100%", (x, y) , font, 1, (0))
#             
#         elif len(approx) == 4:
# #             #         print("Minus")
# #             print("Symbol name = Minus, percentage = 100%")
# #             cv2.putText(resized, "Minus 100%", (x, y), font, 1, (0))
#             (x, y, w, h) = cv2.boundingRect(approx)
#             print("length", x, y, w, h)
#             ar = w / float(h)
#             print("arc", ar)
#             math_img_list.append("Minus")
#             print("Symbol name = Minus, percentage = 100%")
#             cv2.putText(resized, "Minus 100%", (x, y), font, 1, (0))
#              
#         elif len(approx) == 18:
#             print("Symbol name = Multiply, percentage = 100%")
#             #         print("Multiply")
#             cv2.putText(resized, "Multiply 100%", (x, y), font, 1, (0))
#              
#         elif len(approx) == 6:
#             #         print("Division")
#             print("Symbol name = Division, percentage = 100%")
#             cv2.putText(resized, "Division 100%", (x, y), font, 1, (0))
#              
#         elif len(approx) == 7:
# #             print("square root")
#             print("Symbol name = square root, percentage = 100%")
#             cv2.putText(resized, "square root 100%", (x, y), font, 1, (0))
#   
# #     cv2.imshow("shapes", img)
#     cv2.imshow("resized", resized)
# #     cv2.imshow("Threshold", threshold)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# print(len(math_img_list))
# n=len(math_img_list)
# print(math_img_list[1:n])

