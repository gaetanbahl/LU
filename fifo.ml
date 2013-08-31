(*FIFOOOOO*)

type 'a queue =  'a list ref;;

let add x q = q := x::!q ; x ;;

let pop = function q when !q = [] -> failwith "empty queue"
| q -> q := List.rev !q ;
    let x = hd !q in q := (List.rev (tl !q)) ; x;;

let newq () = ref [];;


