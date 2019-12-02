# Data4ML


1. Gao, Ruoyuan and Chirag Shah. “How Fair Can We Go: Detecting the Boundaries of Fairness Optimization in Information Retrieval.” ICTIR (2019).
_although the paper is about fairness, it provides an interesting framework for estimating how much bias exists inherently in the data being used to rerank -- i.e., it develops a way to estimate the upper/lower bounds of achievable fairness. Now, one may consider if a similar approach can be adapted for any LeTOR framework_

2. Jingfang Xu, Chuanliang Chen, Gu Xu, Hang Li, and Elbio Renato Torres Abib. 2010. Improving quality of training data for learning to rank using click-through data. (WSDM '10). http://dx.doi.org/10.1145/1718487.1718509
_This paper covers three aspects of label noise in learning2rank framework. Firstly, label noise deteriorates the model performance. In the paper they only mentioned that the listwise ranking algorithm looks like more robust to label noise but didn't give any insights on why is it the case. Secondly, we can detect label noise by inference from confusion probability p(y/y^*) where y=human labels and y^*=model predicted labels. y^* is predicted from click-through data through a CRF like model p(y^*/click-through). Thirdly, the detected noise is corrected and this correction further enhances the results. They use LETOR datasets and adopt two pairwise and two listwise ranking algos._

3. Trivedi, Harsh & Majumder, Prasenjit. (2016). Noise Correction in Pairwise Document Preferences for Learning to Rank.   
_This paper mention a two phase label noise correction scheme. In the first phase, they do k-fold cross validation to find out a data subset without label noise. They then train a model with purer subsample and use that model for label correction._

4.  Lan, Yanyan. (2014). What Makes Data Robust: A Data Analysis in Learning to Rank.
_This paper investigates an interesting problem of why a same ranking algorithm exhibits varying level of robustness to label noise across datasets. They consider two data metrics : (1) dNoise = proportion of documents with noisy labels, (2) pNoise : Proportion of noisy document pairs. They observe injecting dNoise in dataset would inject varying levels of pNoise in different datasets. They empirically conclude that many algorithms show same trend of performance degradation as pNoise increases in it_
