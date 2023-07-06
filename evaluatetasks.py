import numpy as np
import scipy.stats as st
from scipy.stats import pearsonr, hmean, gmean, spearmanr, rankdata
from sklearn.metrics import auc, roc_curve

def get_arg_parser():
    import argparse

    parser = argparse.ArgumentParser(description='evaluate AMR metric result')
    parser.add_argument('-path_sickdev_prediction_file', type=str, nargs='?',
                                help='path to sick prediction file', required=True)
    
    parser.add_argument('-path_sicktest_prediction_file', type=str, nargs='?',
                                help='path to sick prediction file', required=True)
    
    parser.add_argument('-path_snlidev_prediction_file', type=str, nargs='?',
                                help='path to snli development prediction file', required=True)
    
    parser.add_argument('-path_snlitest_prediction_file', type=str, nargs='?',
                                help='path to snli test prediction file', required=True)
    
    parser.add_argument('-path_multinlimatch_prediction_file', type=str, nargs='?',
                                help='path to multi nli match prediction file', required=True)
    
    parser.add_argument('-path_multinlimismatch_prediction_file', type=str, nargs='?',
                                help='path to multi nli mismatch prediction file', required=True)
    
    parser.add_argument('-path_sickdev_original_file', type=str, nargs='?',
                                help='path to sick orignal tsv file', required=True)
    
    parser.add_argument('-path_sicktest_original_file', type=str, nargs='?',
                                help='path to sick original tsv file', required=True)
    
    parser.add_argument('-path_snlidev_original_file', type=str, nargs='?',
                                help='path to snli development original tsv file', required=True)
    
    parser.add_argument('-path_snlitest_original_file', type=str, nargs='?',
                                help='path to snli test orignal tsv file', required=True)
    
    parser.add_argument('-path_multinlimatch_original_file', type=str, nargs='?',
                                help='path to multi nli match original tsv file', required=True)
    
    parser.add_argument('-path_multinlimismatch_original_file', type=str, nargs='?',
                                help='path to multi nli mismatch orignal tsv file', required=True)
    
    return parser
    
parser = get_arg_parser()
args = parser.parse_args()

# SICK and PARA first graph is ignored (empty graph)
SICKDEV = (args.path_sickdev_original_file, [1, 501])
SICKTEST = (args.path_sicktest_original_file, [1, 4928])
SNLIDEV = (args.path_snlidev_original_file, [1, 10000])
SNLITEST = (args.path_snlitest_original_file, [1, 10000])
MNLIMATCH = (args.path_multinlimatch_original_file, [1, 10000])
MNLIMISMATCH = (args.path_multinlimismatch_original_file, [1, 10000])


def get_predicted_scores(lines, f = lambda x: x.split()[-1], index=SICKTEST[0]):
    out = []
    for i,l in enumerate(lines):
        try:
            x = f(l)
            x = float(x)
            out.append(x)
        except:
            out.append("NA")
    return np.array(out[index[0]:index[1]])  


def readl(p):
    with open(p) as f:
        return f.read().split("\n")


def load_human_scores_mnli_match():
    sts = readl(MNLIMATCH[0])[MNLIMATCH[1][0]:MNLIMATCH[1][1]]
    out = []
    def entailment_mapper(string):
        if string == "CONTRADICTION":
            return 0
        if string == "NEUTRAL":
            return 0
        if string == "ENTAILMENT":
            return 1
        if string == "-":
            return "undecided"
        else:
            error
    for i,l in enumerate(sts):
        x = l.split("\t")[0]
        x = entailment_mapper(x.upper())
        out.append(x)
    return out

def load_human_scores_mnli_mismatch():
    sts = readl(MNLIMISMATCH[0])[MNLIMISMATCH[1][0]:MNLIMISMATCH[1][1]]
    out = []
    def entailment_mapper(string):
        if string == "CONTRADICTION":
            return 0
        if string == "NEUTRAL":
            return 0
        if string == "ENTAILMENT":
            return 1
        if string == "-":
            return "undecided"
        else:
            error
    for i,l in enumerate(sts):
        x = l.split("\t")[0]
        x = entailment_mapper(x.upper())
        out.append(x)
    return out

def load_human_scores_snli_test():
    sts = readl(SNLITEST[0])[SNLITEST[1][0]:SNLITEST[1][1]]
    out = []
    def entailment_mapper(string):
        if string == "CONTRADICTION":
            return 0
        if string == "NEUTRAL":
            return 0
        if string == "ENTAILMENT":
            return 1
        if string == "-":
            return "undecided"
        else:
            error
    for i,l in enumerate(sts):
        x = l.split("\t")[0]
        x = entailment_mapper(x.upper())
        out.append(x)
    return out


def load_human_scores_snli_test_hard():
    sts = readl(SNLITEST[0])[SNLITEST[1][0]:SNLITEST[1][1]]
    out = []
    def entailment_mapper(string):
        if string == "CONTRADICTION":
            return 0
        if string == "NEUTRAL":
            return 0
        if string == "ENTAILMENT":
            return 1
        if string == "-":
            return "undecided"
        else:
            error
    for i, l in enumerate(sts):
        x = l.split("\t")
        s = entailment_mapper(x[0].upper())
        out.append((s, x[-6]))
    import json

    with open('hard_examples/snli_1.0_test_hard.jsonl', 'r') as json_file:
        json_list_str = str(list(json_file))

    keepids = []
    for i, ex in enumerate(out):
        pairid = ex[1]
        if pairid in json_list_str:
            keepids.append(i)
    out = [out[i][0] for i in keepids]
    return out, keepids
        

def load_human_scores_snli_dev():
    sts = readl(SNLIDEV[0])[SNLIDEV[1][0]:SNLIDEV[1][1]]
    out = []
    def entailment_mapper(string):
        if string == "CONTRADICTION":
            return 0
        if string == "NEUTRAL":
            return 0
        if string == "ENTAILMENT":
            return 1
        if string == "-":
            return "undecided"
        else:
            error
    for i,l in enumerate(sts):
        x = l.split("\t")[0]
        x = entailment_mapper(x.upper())
        out.append(x)
    return out

def load_human_scores_sick_dev():
    sts = readl(SICKDEV[0])[SICKDEV[1][0]:SICKDEV[1][1]]
    out = []
    def entailment_mapper(string):
        if string == "CONTRADICTION":
            return 0
        if string == "NEUTRAL":
            return 0
        if string == "ENTAILMENT":
            return 1
    for i,l in enumerate(sts):
        x = l.split("\t")[4]
        x = entailment_mapper(x)
        out.append(x)
    return out

def load_human_scores_sick_test():
    sts = readl(SICKTEST[0])[SICKTEST[1][0]:SICKTEST[1][1]]
    out = []
    def entailment_mapper(string):
        if string == "CONTRADICTION":
            return 0
        if string == "NEUTRAL":
            return 0
        if string == "ENTAILMENT":
            return 1
    for i,l in enumerate(sts):
        x = l.split("\t")[4]
        x = entailment_mapper(x)
        out.append(x)
    return out

def evaluate_with_function(ys, xs, fun):
    return fun(ys, xs)

def area_uc(ys, xs):
    ys = [int(x) for x in ys]
    fpr, tpr, thresholds = roc_curve(ys, xs, pos_label=1)
    return auc(fpr, tpr)


def perc(xs, t=5):
    xsi = enumerate(xs)
    xsi = sorted(xsi, key=lambda x:x[1], reverse=True)
    p = int((len(xsi)/100)*t)
    pxsi = xsi[:p]
    nxsi = xsi[p:]
    new = [0.0] * len(xs)
    for i, _ in pxsi:
        new[i] = 1
    for i, _ in nxsi:
        new[i] = 0
    return new

def acc_of_ones(ys, xs, t=5):
    ys = [int(x) for x in ys]
    xs = perc(xs, t)
    s = 0.0
    for i, x in enumerate(xs):
        if x == 1:
            s += ys[i]
    s /= max(1, sum(xs))
    return s

def acc_of_ones_thres(ys, xs, thres=[1, 2, 3, 4, 5, 7, 10, 15]):
    out = []
    for t in thres:
        out.append(acc_of_ones(ys, xs, t))
    return out

def remove_undecided(gold, pred, returnkeepids=False):
    
    ids = [i for i in range(len(gold)) if gold[i] == "undecided"]
    kids = [i for i in range(len(gold)) if gold[i] != "undecided"]
    gold = [gold[i] for i in range(len(gold)) if i not in ids]
    pred = [pred[i] for i in range(len(pred)) if i not in ids]
     
    if returnkeepids:
        return gold, pred, kids
    
    return gold, pred

if __name__ == "__main__":
    
    human_sickdev = load_human_scores_sick_dev()
    human_sicktest = load_human_scores_sick_test()
    human_snlidev = load_human_scores_snli_dev()
    human_snlitest = load_human_scores_snli_test()
    human_mnlimatch = load_human_scores_mnli_match()
    human_mnlimismatch = load_human_scores_mnli_mismatch()
    
    
    scores = []  

    # default evaluation function
    evalfun = area_uc 
    
    # use this function for evaluating according to thresholds
    #evalfun = acc_of_ones_thres


    path = args.path_sicktest_prediction_file
    pred = get_predicted_scores(readl(path), index=SICKTEST[1])
    human = human_sicktest
    human, pred = remove_undecided(human, pred)
    
    score = evaluate_with_function(human, pred, fun=evalfun)
    scores.append(score)
    print(path, score)
    

    path = args.path_snlidev_prediction_file
    pred = get_predicted_scores(readl(path), index=SNLIDEV[1])
    human = human_snlidev
    human, pred = remove_undecided(human, pred) 
    score = evaluate_with_function(human, pred, fun=evalfun)
    scores.append(score)
    print(path, score)

    path = args.path_snlitest_prediction_file
    pred = get_predicted_scores(readl(path), index=SNLITEST[1])
    
    #UNCOMMENT TO ENABLE HARD EVALUATION
    #human_snlitest, hard_ids = load_human_scores_snli_test_hard()
    #print(len(hard_ids))
    #pred = [pred[i] for i in hard_ids]

    human = human_snlitest
    human, pred = remove_undecided(human, pred)
    
    score = evaluate_with_function(human, pred, fun=evalfun)
    scores.append(score)
    print(path, score)

    path = args.path_multinlimatch_prediction_file
    pred = get_predicted_scores(readl(path), index=MNLIMATCH[1])
    human = human_mnlimatch
    human, pred = remove_undecided(human, pred)

    score = evaluate_with_function(human, pred, fun=evalfun)
    scores.append(score)
    print(path, score)
    
    path = args.path_multinlimismatch_prediction_file
    pred = get_predicted_scores(readl(path), index=MNLIMISMATCH[1])
    human = human_mnlimismatch
    human, pred = remove_undecided(human, pred)

    score = evaluate_with_function(human, pred, fun=evalfun)
    scores.append(score)
    print(path, score)
    
    scores_without_sick = scores[1:]
    
    if isinstance(scores[0], list):
        scores = np.array(scores)
        scores_without_sick = np.mean(scores[1:], axis=0).T
        scores = np.mean(scores, axis=0).T
     
    scores = [round(sc * 100, 1) for sc in scores] + [round(np.mean(scores) * 100, 1)] + [round(np.mean(scores_without_sick) * 100, 1)]
    scores = [str(sc) for sc in scores]
    print("\nmean score", scores[-2])
    print("mean score without SICK", scores[-1])

    scores = " & ".join(scores)
    scores = scores + " \\\\"
    print(scores, "\n")
