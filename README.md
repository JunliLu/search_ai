# Search Tweets by Deep Reinforcement Learning
Search tweets referring to news, by Deep Reinforcement Learning


## Tweet Search Problem
<img src="img/1.png" width="500">


## Search Process
<img src="img/4.png" width="500">

We model search process by Markov Decision Process (MDP) in Reinforcement Learning. \
Please refer to some open materials.

In MDP-based search process, we define

**Immediate Reward**: \
Number of relevant tweets in current search results of tweets. \
(Note that search results are returned by one-time query to a set of tweets)

**State**: \
Difference between current search results (tweets) and previous search results (tweets). \
E.g., one difference value is the difference value between textual contents, modeled by Word2Vec model.

**Reinforcement Learning** \
We learn by Q-learning. \
The loss function for learning:

<img src="https://latex.codecogs.com/gif.latex?(R(s_t,a_t)&plus;\gamma\&space;max_a{Q(s_{t&plus;1},a)}-Q(s_t,a_t))^2" />

*R*: immediate reward \
*Q()*: predicted long-term return \
*s_t*: state at time t \
*a_t*: action (query strategy) used at time t



## Model
### Predict Long-term returns of search process by RNN Model
We use LSTM layer and FC layer \
<img src="img/2.png" width="500">


## Search Results
<img src="img/3.png" width="500">
