# Lyft

## Lifetime Driver 
### Question
Let's say you're given 90 days of ride data.

How would you use it to project the lifetime of a new driver on the system? What about the lifetime value from the driver?

### First thought
- What it is the "lifetime of a new driver"? The duration from start to inactivate?
- How about if the maximum life time more than 90 days?  
- Naturally, the life time may followed the Poisson distribution.

So, first, we should label out which group are experience complete life-time from start to inactive in the 90-day data, and their percentage in the whole dataset. 

The simple way to use this data to train a model to predict if the driver will be inactive during the 90-day or not.  This would be a binary classification problem. The simple classifier could be logistic regression. And be aware of the class imbalance to use the techniques such as downsampling, upsampling, weight adjust.

Another regression model could be used to predict the lifetime of a new driver as simple as linear regression model or Gradient Boosting Tree model.

So, the result could be if the classifier predict the driver would be inactive in 90-day, then to use the predicted lifetime. If predict not be inactive, just ignore the predict the lifetime.


