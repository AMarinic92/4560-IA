import { Problem } from "../interfaces/objects";

const Card = (props:Problem) => {
    return ( 
        <div className="flex flex-row  mb-5">
            <img
                src={props.imageUrl}
                alt=""
                width={90}
                height={90}
                style={
                    {
                        objectFit:"contain"
                    }
                }
            >
            </img>
            <div className="flex flex-col prose">
                    <p className="font-bold"> Type: {props.type}</p>
                    <p className="font-bold">Suggestion: {props.suggestion}</p>
            </div>

        </div>
     );
}
 
export default Card;