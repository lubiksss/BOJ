for key in tqdm(dhash_dict):
    if len(dhash_dict[key]) > 1:
        #         print(len(dhash_dict[key]))
        #         print(len(list(combinations(dhash_dict[key],2))))
        for case in list(combinations(dhash_dict[key], 2)):
            try:
                img1 = Image.open(IMG_LOAD_PATH+case[0]).convert('RGB')
    #             img1.show()
    #             print(case[0])
    #             print(img1.size)
                img1_t = tf(img1).unsqueeze(dim=0).to('cuda')

                img2 = Image.open(IMG_LOAD_PATH+case[1]).convert('RGB')
    #             img2.show()
    #             print(case[1])
    #             print(img2.size)
                img2_t = tf(img2).unsqueeze(dim=0).to('cuda')

                score = D(img1_t, img2_t, as_loss=False)[0]
    #             print(score)

    #             print('-----------------------------------------------------------')
            except RuntimeError as e:
                print(e)
                img1 = Image.open(IMG_LOAD_PATH+case[0])
                img2 = Image.open(IMG_LOAD_PATH+case[1])
                print(case[0], len(img1.split()), img1.size)
                print(case[1], len(img2.split()), img2.size)
                break

            dhash_score += score
            dhash_cnt += 1

#         print(ahash_score/ahash_cnt)
