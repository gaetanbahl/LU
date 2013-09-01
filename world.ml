(*PLANETS N ANIMALS N STUFF*)

#use "fifo.ml"


module World = struct (*should we abstract everything ?*)

    type coordinates = float * float
    type type_coord = Spheriques | Cartesiennes
    
    type biome = Desert | Foret | Ocean
    type biome_spot = {type_biome : biome ;
        pos : coordinates ;
        power : float}
    
    type resource = Food | Water | Material | Nothing

    type resource_point = coordinates * resource * int

    type lu = (string -> string Q.queue ) * int
    (*more types*)

     


    (*WHAT IF... WHAT IF WE MADE EVERYTHING WITH PARTIAL FUNCTIONS ? o_o AWESOME BOOOP BOOP*)
    (*ou pas en fait, terrible idea*)
    
       
    let lifeunit coord str =
    begin
        let pos = ref coord in
        let actions = Q.newq () in
        let carry = ref Nothing in

        (*on enregitre les actions d'IA dans la queue puis on renvoie la queue*)
        
        actions
        
    end
        
    let world r crd () =
    begin
        let rayon = r in
        let coord = crd in
        let biomes = ref [] in
        let lifeunits = ref [] in (*liste de fonctions*id *)
        let resources_points = ref [] in (*liste de fonctions*id *)
        let actions = Q.newq () in
        let last_id_lu = ref 0 in (*On garde un int avec le nombre de LU car compter le nombre de LU dans une liste est couteux*)

        let new_lu pos = lifeunits := (lifeunit pos)::(!lifeunits) in
            (*et là on mettra des machins qui utilisent la queue*)
    end



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

    


    let rec del_lu = fun
    [] _ -> failwith "No such id"
    | h::q i when h = i -> q
    | h::q i -> del_lu_id q i

   
        
end;;
