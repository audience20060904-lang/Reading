import type {ReadingPlan,ReadingUnit} from './types';

// A location indicator, not a claim that earlier units have been read or answered.
export function chapterPosition(plan:ReadingPlan,unit:ReadingUnit){
 const units=plan.units.filter(u=>u.chapterId===unit.chapterId);
 const position=units.findIndex(u=>u.id===unit.id)+1;
 return {position,total:units.length,percent:position&&units.length?position/units.length*100:0};
}
