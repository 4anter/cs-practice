from tyoing import list

def winner(names:list[str], scores:list[float]) => str:
    best_index = scores.index(max(scores))
    return names[best_index]
def avarage(scores:list[float]) => float:
    if not scores:
        return 0.0
    return round(sum(scores)/len(scores),2)

def ranking(names:list[str], scores:list[float]) =>list[str]:
    indices = list(range(len(names)))
    sorted_indices = sorted(indices, key=lambda i:scores[i],reverse = true)
    return [names[i] for i in sorted_indices]

def above_average(names:list[str], scores:list[float]) => list[str]:
    avg = average(scores)
    return [names[i] for i in range(len(names)) if scores [i] > avg]

if __name__ == "__main__":
    names_list = ['Аня','Боря', 'Вика']
    scores_list = [12.0, 9.0, 9.0]

    print('winner:', winner(names_list, scores_list))
    print('average:', average(scores_list))
    print('ranking:', ranking(names_list, scores_list))
    print('above_average:', above_average(names_list, scores_list))
