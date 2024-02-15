import { useEffect, useState } from "react";
import { Suggestion } from "../interfaces/objects";

const Suggestions = () => {
    const [suggestions, setSuggestions] = useState<Suggestion[]>([])
    
    useEffect(
        ()=>{
            setSuggestions([{ id: "1", type: "missing alt text", message: "possible alt text could be  `dancing dog` " }])
        }
        ,[]
    )

    return (
        <div tabIndex={0} className="collapse collapse-arrow border border-base-300 bg-primary mb-2">
              <input type="checkbox" />
            <div className="collapse-title text-xl font-medium">
                Suggestions
            </div>
            <div className="collapse-content">
            {
                    suggestions.map(
                        (suggestion: Suggestion) => {
                            return (
                                <div className="flex flex-row w-full justify-between  mb-2" key={suggestion.id}>
                                    <p className="font-bold capitalize">{suggestion.type}</p>
                                    <p>{suggestion.message}</p>
                                    <div className="divider" />
                                </div>
                            )
                        }
                    )
                }
            </div>
        </div>
    )
}

export default Suggestions;