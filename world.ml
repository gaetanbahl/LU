(*PLANETS N ANIMALS N STUFF*)

#use "fifo.ml"


module World = struct (*should we abstract everything ?*)

    type coordinates = float * float
    type type_coord = Spheriques | Cartesiennes
    
    type lifeunit = {pos : coordinates ; actions : string Q.queue} 
    type biome = Desert | Foret | Ocean
    type biome_spot = {type_biome : biome ;  pos : coordinates ; power : float}
    type resource = Food | Water | Material
    type resource_point = {pos : coordinates ; res_type : resource}
    type world = {rayon : int ; coord : type_coord ; biomes : biome list ; lifeunits : lifeunit list}

    let sq x = x*.x
     
    let distance a b world = match a.pos,b.pos,world.coord with
        (phia,thetaa),(phib,thetab),Spheriques ->
            acos ((sin phia)*.(sin phib) +. (cos phia)*.(cos phib)*.(cos(thetab -. thetaa)))         (*http://fr.wikipedia.org/wiki/Orthodromie*)
        |(xa,ya),(xb,yb),Cartesiennes -> sqrt (sq(xb -. xa) +. sq(yb -. ya))

end;;
