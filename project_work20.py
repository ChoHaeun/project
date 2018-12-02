import requests
url = 'https://movie.naver.com/movie/sdb/rank/rreserve.nhn' 
r = requests.get(url)

data = str(r.text)


print('<영화 예매 랭킹 Top 10>')
print()

for i in range (1,11):
    begin1=data.find('alt="0'+str(i)+'"')
    if i==10:
        begin1=data.find('alt="10"')
    name1=data[begin1+140:begin1+140+150]
    end1=name1.find('">')
    r_begin1=name1.find('"reserve_per ar">')
    r_end1=name1.find('%<')
    print(str(i)+'위>>',name1[:end1])
    print('*예매율:',name1[r_begin1+17:r_end1+1])
    lank1=data[begin1:begin1+140]
    inform1=lank1.find('/movie/bi/mi/basic.nhn?code=')
    url1= 'https://movie.naver.com'
    inform1_url=url1+lank1[inform1:inform1+34]
    r1= requests.get(inform1_url)
    data1=str(r1.text)

    release_end=data1.find('</a> 개봉')
    release_y=data1[release_end-16:release_end-12]
    release_md=data1[release_end-5:release_end]
    print('*개봉일: %s.%s' %(release_y[:4], release_md))

    gstar_begin=data1.find('<em class="blind">관람객 평점')
    if gstar_begin==-1:
        print('*관람객 평점: 0.00★')
    if gstar_begin!=-1:
        gstar_end=data1.find('<em class="blind">기자 &middot; 평론가 평점')
        gstar=data1[gstar_begin:gstar_end]
        gstar_print=gstar.find('width:')
        if float(gstar[gstar_print+6:gstar_print+7])==0:
            print('*관람객 평점: 0.00★')
        if float(gstar[gstar_print+6:gstar_print+7])!=0:
            gstar_inform=gstar[gstar_print+6:gstar_print+6+4]
            print('*관람객 평점: %4.2f★' %(float(gstar_inform)*0.1))

    pstar_begin=gstar_end
    if pstar_begin==-1:
        print('*평론가 평점: 0.00★')
    if pstar_begin!=-1:
        pstar_end=data1.find('<em class="blind">네티즌 평점')
        pstar=data1[pstar_begin:pstar_end]

        pstar_print=pstar.find('width:')
        if float(pstar[pstar_print+6:pstar_print+7])==0:
            pirnt('*평론가 평점: 0.00★')

        if float(pstar[pstar_print+6:pstar_print+7])!=0:
            pstar_inform=pstar[pstar_print+6:pstar_print+6+4]
            print('*평론가 평점: %4.2f★' %(float(pstar_inform)*0.1))
    print()
