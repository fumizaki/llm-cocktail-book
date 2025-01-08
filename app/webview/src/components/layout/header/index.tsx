import { cn } from '@/lib/style';
import { HeaderDropdown } from './dropdown';

export const Header = ({ className }: { className?: string }) => {
    return (
        <header
            className={cn(
                'w-full h-20 flex justify-between items-center text-primary bg-slate-100 dark:bg-slate-950 border-b border-slate-300 dark:border-slate-300',
                className,
            )}
        >
            <div className={'flex items-center gap-2 pl-4'}>
                <h2>LLM Cocktail Book</h2>
            </div>
            <div className={'pr-8'}>
                <HeaderDropdown/>
            </div>
        </header>
    );
};