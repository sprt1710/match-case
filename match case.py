

while True:
    menue=input("1.restruant , 2.cafe , 3.fast food , 4.game board , 5.exit")

    while True:
        match_menue:

            case "1":
        
                menu_restruant=input("1.kabab 700  2.khoresh 500  3.khorak 400  4.dogh 100: ")
                match menu_restruant:
                    case "1":
                        num_kabab=int(input("chanta mikhay?"))
                        price_kabab=num_kabab*700*1.1
                        print:"("kabab     ")
                    case "2":
                        tedad_khoresh=int(input("chanta mikhay?"))
                        price_khoresh=tedad_khoresh*500*1.1
                        print:"hazine",   ,"mishavad"
                case "3":
                        tedad_khorak=int(input("chanta mikhay?"))
                        price_khorak=tedad_khorak*400*1.1
                        print:"hazine",   ,"mishavad"
                case "4":
                tedad_dogh=int(input("chanta mikhay?"))
                price_dogh=tedad_dogh*100*1.1
                print:"hazine",   ,"mishavad"
                case_:
                break


            case "2":
            menu_cafe=input("1.ghahve 200, 2.cake 250 , 3.bastani 150 , 4.abmive 100 ")
                case "1":
            