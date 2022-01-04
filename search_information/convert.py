import json

f_chinh_tri = open('chinhphu/chinh_tri.json', 'r', encoding='utf-8-sig')
f_khoa_giao = open('chinhphu/khoa_giao.json', 'r', encoding='utf-8-sig')
f_kinh_te = open('chinhphu/kinh_te.json', 'r', encoding='utf-8-sig')
f_quoc_te = open('chinhphu/quoc_te.json', 'r', encoding='utf-8-sig')
f_van_hoa = open('chinhphu/van_hoa.json', 'r', encoding='utf-8-sig')
f_xa_hoi = open('chinhphu/xa_hoi.json', 'r', encoding='utf-8-sig')

f_tt_gia_that = open('tuoitre/gia_that.json', 'r', encoding='utf-8-sig')
f_tt_giai_tri = open('tuoitre/giai_tri.json', 'r', encoding='utf-8-sig')
f_tt_giao_duc = open('tuoitre/giao_duc.json', 'r', encoding='utf-8-sig')
f_tt_khoa_hoc = open('tuoitre/khoa_hoc.json', 'r', encoding='utf-8-sig')
f_tt_kinh_doanh = open('tuoitre/kinh_doanh.json', 'r', encoding='utf-8-sig')
f_tt_nhip_song_tre = open('tuoitre/nhip_song_tre.json', 'r', encoding='utf-8-sig')
f_tt_phap_luat = open('tuoitre/phap_luat.json', 'r', encoding='utf-8-sig')
f_tt_suc_khoe = open('tuoitre/suc_khoe.json', 'r', encoding='utf-8-sig')
f_tt_the_gioi = open('tuoitre/the_gioi.json', 'r', encoding='utf-8-sig')
f_tt_the_thao = open('tuoitre/the_thao.json', 'r', encoding='utf-8-sig')
f_tt_thoi_su = open('tuoitre/thoi_su.json', 'r', encoding='utf-8-sig')
f_tt_van_hoa = open('tuoitre/van_hoa.json', 'r', encoding='utf-8-sig')
f_tt_xe = open('tuoitre/xe.json', 'r', encoding='utf-8-sig')

chinh_tri = json.load(f_chinh_tri)
khoa_giao = json.load(f_khoa_giao)
kinh_te = json.load(f_kinh_te)
quoc_te = json.load(f_quoc_te)
van_hoa = json.load(f_van_hoa)
xa_hoi = json.load(f_xa_hoi) 

tt_gia_that = json.load(f_tt_gia_that) 
tt_giai_tri = json.load(f_tt_giai_tri) 
tt_giao_duc = json.load(f_tt_giao_duc) 
tt_khoa_hoc = json.load(f_tt_khoa_hoc) 
tt_kinh_doanh = json.load(f_tt_kinh_doanh)
tt_nhip_song_tre = json.load(f_tt_nhip_song_tre)
tt_phap_luat = json.load(f_tt_phap_luat)
tt_suc_khoe = json.load(f_tt_suc_khoe) 
tt_the_gioi = json.load(f_tt_the_gioi) 
tt_the_thao = json.load(f_tt_the_thao) 
tt_thoi_su = json.load(f_tt_thoi_su) 
tt_van_hoa = json.load(f_tt_van_hoa) 
tt_xe = json.load(f_tt_xe) 

news = [chinh_tri, khoa_giao, kinh_te, quoc_te, van_hoa, xa_hoi, tt_gia_that, tt_giai_tri
        ,tt_giao_duc, tt_khoa_hoc, tt_kinh_doanh, tt_nhip_song_tre, tt_phap_luat, tt_suc_khoe
        , tt_the_gioi, tt_the_thao, tt_thoi_su, tt_van_hoa, tt_xe]


data = open('data.txt', 'w', encoding='utf-8-sig')
id = 0

for new in news:
    for i in new:
        tmp = "{\"index\": {\"_index\": \"search_machine\", \"_id\": "+ str(id)+"}}"
        data.write(tmp)
        data.write("\n")
        tmp = json.dumps(i, ensure_ascii=False)

        #tmp = "{\"path\": \""+i['path'] + "\", \"title\": \""+""+i['title']+"\", \"content\": \""+i['content']+"\", \"time\": \""+i['time']+"\"}"
        data.write(tmp)


        data.write("\n")
        id = id+1
    
f_chinh_tri.close()
f_khoa_giao.close()
f_kinh_te.close()
f_quoc_te.close()
f_van_hoa.close()
f_xa_hoi.close()

f_tt_gia_that.close()
f_tt_giai_tri.close()
f_tt_giao_duc.close()
f_tt_khoa_hoc.close()
f_tt_kinh_doanh.close()
f_tt_nhip_song_tre.close()
f_tt_phap_luat.close()
f_tt_suc_khoe.close()
f_tt_the_gioi.close()
f_tt_the_thao.close()
f_tt_thoi_su.close()
f_tt_van_hoa.close()
f_tt_xe.close()
data.close()