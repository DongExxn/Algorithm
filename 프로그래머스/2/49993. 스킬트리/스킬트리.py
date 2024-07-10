def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        skill_index = 0
        
        for s in skill_tree:
            if s in skill:
                if s == skill[skill_index]:
                    skill_index += 1
                else:
                    break
        else:
            answer += 1
            
    return answer
