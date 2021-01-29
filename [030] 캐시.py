#210129 캐시
def solution(cacheSize, cities):
    cities = [i.lower() for i in cities]
    time = 5
    cache = [cities[0]]
    if cacheSize == 0 :
        time += 5 * (len(cities) -1)
    else :
        for i in cities[1:] :
            if len(cache) < cacheSize and i in cache: 
                cache.pop(cache.index(i))
                time += 1
            elif len(cache) < cacheSize :
                time += 5
            elif i in cache :
                cache.pop(cache.index(i))
                time += 1
            else :
                del cache[0]
                time += 5
            cache.append(i)
    return time

print(solution(0, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA'])) #25