(*FIFOOOOO*)

module Q = struct

    type 'a queue =  'a list ref;;

    let add x q = q := x::!q ; x ;;

    let pop = function q when !q = [] -> failwith "empty queue"
        | q -> q := List.rev !q ;
            let x = List.hd !q in q := (List.rev (List.tl !q)) ; x;;

    let newq () = ref [];;

    let rec empty_in a b = match !a with
    [] -> failwith "empty queue"
    | h::q -> add (pop a) b;;
    

end ;;

