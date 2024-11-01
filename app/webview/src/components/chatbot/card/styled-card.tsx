import { cn } from '@/lib/style';
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from '@/components/ui/card';

export const StyledCard = ({ children, className }: { children: React.ReactNode; className?: string }) => {
    return (
        <Card
            className={cn(
                'flex flex-col gap-4 h-fit w-full bg-gray-50 dark:bg-gray-950 border border-gray-400 dark:border-gray-600',
                className,
            )}
        >
            {children}
        </Card>
    );
};

export const StyledCardHeader = ({ children, className }: { children: React.ReactNode; className?: string }) => {
    return (
        <CardHeader
            className={cn(
                'flex flex-row justify-between items-center px-4 py-2 space-y-0 rounded-t-lg border-b border-gray-400 dark:border-gray-600 bg-gray-200 dark:bg-gray-800',
                className,
            )}
        >
            {children}
        </CardHeader>
    );
};

export const StyledCardTitle = ({ children, className }: { children: React.ReactNode; className?: string }) => {
    return (
        <CardTitle className={cn('text-md font-semibold text-gray-700 dark:text-gray-300', className)}>
            {children}
        </CardTitle>
    );
};

export const StyledCardBody = ({ children, className }: { children: React.ReactNode; className?: string }) => {
    return (
        <CardContent
            className={cn(
                'flex flex-col h-full gap-4 px-4 py-2 text-sm font-semibold text-slate-800 dark:text-slate-100 overflow-auto',
                className,
            )}
        >
            {children}
        </CardContent>
    );
};

export const StyledCardItem = ({ label, children }: { label: string; children: React.ReactNode }) => {
    return (
        <div className={'flex flex-col gap-2'}>
            <p className={'py-2 text-gray-700 dark:text-gray-400 border-b border-gray-400'}>{label}</p>
            {children}
        </div>
    );
};

export const StyledCardFooter = ({ children, className }: { children: React.ReactNode; className?: string }) => {
    return (
        <CardFooter
            className={cn(
                'flex flex-row justify-between items-center px-4 py-2 space-y-0 border-t border-gray-400 dark:border-gray-600',
                className,
            )}
        >
            {children}
        </CardFooter>
    );
};