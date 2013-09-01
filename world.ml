(*PLANETS N ANIMALS N STUFF*)

#use "fifo.ml"


module World = struct (*should we abstract everything ?*)

    type coordinates = float * float
    type type_coord = Spheriques | Cartesiennes
    
    type lifeunit = {id : int ;
        mutable pos : coordinates ;
        mutable actions : string Q.queue ;
        mutable carry : resource}
    
    type biome = Desert | Foret | Ocean
    type biome_spot = {type_biome : biome ;
        pos : coordinates ;
        power : float}
    
    type resource = Food | Water | Material | Nothing
    type resource_point = {pos : coordinates ;
        res_type : resource ;
        mutable number : int}
    
    type world = {rayon : int ; coord : type_coord ;
        mutable biomes : biome list ;
        mutable lifeunits : lifeunit*coordinates list
        mutable resources_points : resource_point list
        mutable actions : string Q.queue}

    let sq x = x*.x
     
    let distance_objets a b coord_type = match a.pos,b.pos,coord_type with
        (phia,thetaa),(phib,thetab),Spheriques ->
            acos ((sin phia)*.(sin phib) +. (cos phia)*.(cos phib)*.(cos(thetab -. thetaa)))
            (*http://fr.wikipedia.org/wiki/Orthodromie*)
        |(xa,ya),(xb,yb),Cartesiennes -> sqrt (sq(xb -. xa) +. sq(yb -. ya))

    let distance obj pt coord_type = match obj.pos,pt,coord_type with
        (phia,thetaa),(phib,thetab),Spheriques ->
            acos ((sin phia)*.(sin phib) +. (cos phia)*.(cos phib)*.(cos(thetab -. thetaa)))
        |(xa,ya),(xb,yb),Cartesiennes -> sqrt (sq(xb -. xa) +. sq(yb -. ya))
            
    let move_sph lu,dest spd  =
        lu.pos <- ((((fst dest) -. (fst lu.pos))*.spd )/.(distance lu dest Sphériques)),
        ((((snd dest) -. (snd lu.pos))*.spd)/.(distance lu dest Spheriques)) ;; (*Thalès*)

    let move_cart lu,dest spd  =
        lu.pos <- ((((fst dest) -. (fst lu.pos))*.spd )/.(distance lu dest Cartesiennes)),
        ((((snd dest) -. (snd lu.pos))*.spd)/.(distance lu dest Cartesiennes)) ;;

end;;
