from sklearn import linear_model
import os

print "Test Started"
logistic = linear_model.LogisticRegression()
print logistic
print os.environ['LOG_FILE']
print "Test Ended"
