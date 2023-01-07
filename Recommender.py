from surprise import KNNBasic
import pandas as pd
from surprise import Dataset
from surprise import Reader

def do_Predict():

    userList = ['thomas', 'peter', 'thomas', 'peter']
    itemList = ['avatar', 'harry potter', 'the hobbit', 'avatar']
    ratingList = [5, 3, 4, 5]


    ratings_dict = {'user': userList,
                    'item': itemList,
                    'rating': ratingList}

    df = pd.DataFrame(ratings_dict)
    reader = Reader(rating_scale=(0, 5))
    data = Dataset.load_from_df(df[['user', 'item', 'rating']], reader)
    trainset = data.build_full_trainset()

    algo = KNNBasic()
    algo.fit(trainset)

#Here the user and item input is given for what you would like to predict. in this
#example we want to predict the rating that Thomas would give to the hobbit based on previous view data
#if the prediction is high, it's likly that he would like the movie and we can recommend it to him, if not we might want to display/recommend
#another movie for him.
    pred = algo.predict('thomas', 'the hobbit', verbose=True)


    return(pred)