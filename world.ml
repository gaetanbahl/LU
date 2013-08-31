(*PLANETS N ANIMALS N STUFF*)

#use "fifo.ml"


module World = struct (*should we abstract everything ?*)

    type coordinates = float * float
    type type_coord = Spheriques | Cartesiennes
    
    type bestiole = {pos : coordinates ; actions : string Q.queue} 
    type biome = Desert | Foret | Ocean
    type biome_spot = {type_biome : biome ;  pos : coordinates ; power : float}
    type world = {rayon : int ; coord : type_coord ; biomes : biome list ; bestioles : bestiole list}

    let sq x = x*.x
     
    let distance a b world = match a.pos,b.pos,world.coord with
        (phia,thetaa),(phib,thetab),Spheriques ->
            acos ((sin phia)*.(sin phib) +. (cos phia)*.(cos phib)*.(cos(thetab -. thetaa)))         (*http://fr.wikipedia.org/wiki/Orthodromie*)
        |(xa,ya),(xb,yb),Cartesiennes -> sqrt (sq(xb -. xa) +. sq(yb -. ya))

end;;
