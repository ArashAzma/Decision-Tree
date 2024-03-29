import turtle
from Node import Node, LeafNode
import numpy as np
import pandas as pd
from functions import entropy, informationGain

class Tree:
    # constructure
    def __init__(self, depth=10):
        self.depth = depth
        self.root = Node()

    @staticmethod
    def Entropy(labels):
       return entropy(labels)
    
    def drawRectangle(width, value, attribute, x, y):
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.setx(x)
        pen.sety(y)
        pen.pendown()
        for i in range(4):
            pen.forward(width)
            pen.right(90)
        pen.write(value)
        pen.up()
        pen.sety(y - width/2)
        pen.setx(x + width/4)
        pen.down
        pen.write(attribute)
            
    def movePen(x1, y1, x2, y2, width):
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.up()
        pen.setx(x1 + width/2)
        pen.sety(y1 - width)
        pen.down()
        pen.setpos(x2+width/2, y2)
    
    def drawTree(depth , root, x, y, width, screenWidth, screenHeight, colors, outputs) :
        
        if(root.value == -1) :
            for xx in root.labels:
                found = False
                for yy in outputs:
                    if yy == xx:
                        found = True
                        break
                if not found:
                    outputs.append(xx)
        print(outputs)
        dy = screenHeight/depth
        turtle.screensize(canvwidth=screenWidth, canvheight=screenHeight, bg="white") 
        if root.isFeature or not root.isLeaf :
            Tree.drawRectangle(width, root.value, root.featureName, x, y)
            
            pen = turtle.Turtle()
            xPos = x - 15
            yPos = y
            pen.up()
            pen.setpos(x, y)
            pen.hideturtle()
            pen.speed(0)
            for i in range (0, len(root.labels)):  
                for j in range (0, len(outputs)) :
                    if(root.labels[i] == outputs[j]) :
                        pen.fillcolor(colors[j])
                        xPos += 10
                        pen.begin_fill()
                        pen.setpos(xPos, yPos)
                        pen.down()
                        pen.circle(3)
                        pen.end_fill()
                        pen.up()
                        print(root.labels[i])
                        break
    
            dx = (screenWidth-50)/len(root.children)
            for i in range(0, len(root.children)):
                x0 = x-70+10*i
                Tree.movePen(x, y, x0+60*i , y-dy,width)
                Tree.drawTree(depth, root.children[i],x0+60*i,y-dy,width,screenWidth,screenHeight, colors, outputs)
        
        elif root.isLeaf :
            Tree.drawRectangle(width, root.value, "" , x, y)
                    
            pen = turtle.Turtle()
            xPos = x
            yPos = y
            pen.up()
            pen.setpos(x, y)
            pen.hideturtle()
            pen.speed(0)
            color = ""
            for j in range (0 , len(outputs)) :
                if(outputs[j] == root.label) :
                    color = colors[j]
            pen.fillcolor(color)
            for i in range (0, root.labelLength) :
                xPos += 10
                pen.begin_fill()
                pen.setpos(xPos, yPos)
                pen.down()
                pen.circle(3)
                pen.end_fill()
                pen.up()
                
    @staticmethod
    def iGain(data, labels):
        return informationGain(data, labels)
    
    def best_split(self, data, labels):
        best_feature_name = None
        best_gain = -1

        for feature in data.columns:
            gain = self.iGain(data[feature], labels)

            if gain > best_gain:
                best_gain = gain
                best_feature_name = feature

        return best_feature_name

    def createTree(self, data, label, root = None):

        if root is None: 
            root = Node(data, label)
            self.root = root

        labelsArray = np.array(label)

        if self.Entropy(labelsArray) == 0 or data.empty or label.empty: 
            return

        bestSplitColumnName = self.best_split(data, label)
        uniqueValues = data[bestSplitColumnName].unique()
        
        root.featureName = bestSplitColumnName

        for value in uniqueValues:
            subset_indices = data[bestSplitColumnName] == value
            subsetArray = np.array(subset_indices)

            droppedColumnData = data.drop(bestSplitColumnName, axis = 1)
            
            dataArray = np.array(droppedColumnData)

            labelSubset = [labelsArray[i] for i, subIndex in enumerate(subsetArray) if subIndex]
            dataSubset = [dataArray[i] for i, subIndex in enumerate(subsetArray) if subIndex]


            if(self.isLeafNode(labelSubset)):
                node = LeafNode(value, labelSubset[0], len(labelSubset))
                root.children.append(node)  
            
            else:
                node = Node(dataSubset, labelSubset, "", value)
                label_subset_df = pd.DataFrame({'label': labelSubset})
                data_subset_df = pd.DataFrame(dataSubset, columns=droppedColumnData.columns)
                root.children.append(node)
                self.createTree(data_subset_df, label_subset_df['label'], node)


    def isLeafNode(self, label):
        return self.Entropy(label) == 0

